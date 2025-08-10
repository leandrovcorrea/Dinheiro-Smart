import React, { createContext, useContext, useState, useEffect, useMemo, useCallback } from 'react';

const PortfolioContext = createContext();

export const usePortfolio = () => {
    const context = useContext(PortfolioContext);
    if (!context) throw new Error('usePortfolio must be used within a PortfolioProvider');
    return context;
};

export const PortfolioProvider = ({ children }) => {
    const [transactions, setTransactions] = useState([]);
    const [prices, setPrices] = useState({});
    const [isLoadingPrices, setIsLoadingPrices] = useState(true);
    const [rechartsReady, setRechartsReady] = useState(false);
    const [rechartsError, setRechartsError] = useState(false);
    const [apiStatus, setApiStatus] = useState('');

    useEffect(() => {
        if (window.Recharts) {
            setRechartsReady(true);
            return;
        }
        const script = document.createElement('script');
        script.src = "https://unpkg.com/recharts@2.12.7/umd/Recharts.min.js";
        script.async = true;
        script.onload = () => setRechartsReady(true);
        script.onerror = () => setRechartsError(true);
        document.body.appendChild(script);
        return () => {
            if (document.body.contains(script)) {
                document.body.removeChild(script);
            }
        };
    }, []);

    const handleSaveTransaction = useCallback((transactionData) => {
        setTransactions(current => [...current, transactionData]);
    }, []);

    const handleImportTransactions = useCallback((importedTransactions) => {
        setTransactions(current => [...current, ...importedTransactions]);
    }, []);

    const handleDeleteAsset = useCallback((tickerToDelete) => {
        if (window.confirm(`Tem certeza que deseja excluir ${tickerToDelete}?`)) {
            setTransactions(current => current.filter(t => t.ticker !== tickerToDelete));
        }
    }, []);

    const portfolio = useMemo(() => {
        const transactionsByTicker = transactions.reduce((acc, t) => {
            if (t.type === 'Dividendo') return acc;
            acc[t.ticker] = acc[t.ticker] || [];
            acc[t.ticker].push(t);
            return acc;
        }, {});

        return Object.entries(transactionsByTicker).map(([ticker, tickerTransactions]) => {
            tickerTransactions.sort((a, b) => new Date(a.date) - new Date(b.date));
            let totalQuantity = 0, totalCost = 0, assetInfo = {}, totalQuantityBought = 0;
            for (const t of tickerTransactions) {
                if (!assetInfo.type) assetInfo = t.assetInfo;
                if (t.type === 'Compra') {
                    totalCost += t.quantity * t.price;
                    totalQuantity += t.quantity;
                    totalQuantityBought += t.quantity;
                } else {
                    totalQuantity -= t.quantity;
                }
            }
            if (totalQuantity <= 0) return null;
            const avgPrice = totalQuantityBought > 0 ? totalCost / totalQuantityBought : 0;
            return { ticker, quantity: totalQuantity, avgPrice, type: assetInfo.type, country: assetInfo.country };
        }).filter(Boolean);
    }, [transactions]);

    const financialSummary = useMemo(() => {
        const sortedTransactions = [...transactions].sort((a, b) => new Date(a.date) - new Date(b.date));
        let totalDividends = 0, realizedGains = 0, realizedLosses = 0;
        const holdings = {};
        for (const t of sortedTransactions) {
            if (t.type === 'Dividendo') {
                totalDividends += t.price;
                continue;
            }
            if (!holdings[t.ticker]) holdings[t.ticker] = { quantity: 0, totalCost: 0 };
            if (t.type === 'Compra') {
                holdings[t.ticker].quantity += t.quantity;
                holdings[t.ticker].totalCost += t.quantity * t.price;
            } else if (t.type === 'Venda') {
                if (holdings[t.ticker]?.quantity > 0) {
                    const avgCost = holdings[t.ticker].totalCost / holdings[t.ticker].quantity;
                    const pnl = (t.price - avgCost) * t.quantity;
                    if (pnl > 0) realizedGains += pnl; else realizedLosses += pnl;
                    holdings[t.ticker].totalCost -= avgCost * t.quantity;
                    holdings[t.ticker].quantity -= t.quantity;
                }
            }
        }
        return { totalDividends, realizedGains, realizedLosses };
    }, [transactions]);

    useEffect(() => {
        const fetchPrices = async () => {
            if (portfolio.length === 0) {
                setIsLoadingPrices(false);
                setPrices({});
                setApiStatus('');
                return;
            }
            setIsLoadingPrices(true);
            setApiStatus('Atualizando cotações...');
            const tickers = portfolio.map(asset => asset.ticker).join(',');
            try {
                const response = await fetch(`https://brapi.dev/api/quote/${tickers}`);
                const data = await response.json();
                const results = data.results || [];
                const newPrices = results.reduce((acc, r) => {
                    if (r.regularMarketPrice) acc[r.symbol] = r.regularMarketPrice;
                    return acc;
                }, {});
                setPrices(newPrices);
                setApiStatus(`Cotações atualizadas às ${new Date().toLocaleTimeString()}`);
            } catch {
                setApiStatus('Erro ao obter cotações. Usando preço médio.');
            } finally {
                setIsLoadingPrices(false);
            }
        };

        fetchPrices();
        const intervalId = setInterval(fetchPrices, 60000);
        return () => clearInterval(intervalId);
    }, [portfolio]);

    return (
        <PortfolioContext.Provider value={{
            transactions,
            portfolio,
            prices,
            isLoadingPrices,
            financialSummary,
            rechartsReady,
            rechartsError,
            apiStatus,
            handleSaveTransaction,
            handleDeleteAsset,
            handleImportTransactions,
        }}>
            {children}
        </PortfolioContext.Provider>
    );
};