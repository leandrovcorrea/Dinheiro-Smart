import React, { useState } from 'react';
import { usePortfolio } from '../context/PortfolioContext';
import AssetCard from '../components/AssetCard';
import TransactionModal from '../components/TransactionModal';
import ImportModal from '../components/ImportModal';
import { Upload, Download, PlusCircle, Briefcase } from 'lucide-react';

const Investments = () => {
    const {
        portfolio,
        prices,
        isLoadingPrices,
        handleDeleteAsset,
        handleSaveTransaction,
        handleImportTransactions,
        transactions
    } = usePortfolio();

    const [isTransactionModalOpen, setTransactionModalOpen] = useState(false);
    const [isImportModalOpen, setImportModalOpen] = useState(false);

    const handleExportTransactions = () => {
        if (transactions.length === 0) {
            console.warn("Não há transações para exportar.");
            return;
        }
        const headers = ['tipo', 'data', 'ticker', 'quantidade', 'preco'];
        const csvContent = [
            headers.join(','),
            ...transactions.map(t => [t.type, t.date, t.ticker, t.quantity, t.price].join(','))
        ].join('\n');
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement("a");
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", "carteira_dinheirosmart.csv");
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold text-gray-800 dark:text-white">Meus Investimentos</h1>
                <div className="flex space-x-2">
                    <button onClick={() => setImportModalOpen(true)} className="flex items-center space-x-2 bg-gray-600 text-white px-4 py-2 rounded-lg hover:bg-gray-700 transition-colors duration-300 shadow">
                        <Upload size={20} />
                        <span>Importar</span>
                    </button>
                    <button onClick={handleExportTransactions} className="flex items-center space-x-2 bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors duration-300 shadow">
                        <Download size={20} />
                        <span>Exportar</span>
                    </button>
                    <button onClick={() => setTransactionModalOpen(true)} className="flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors duration-300 shadow">
                        <PlusCircle size={20} />
                        <span>Adicionar</span>
                    </button>
                </div>
            </div>

            {portfolio.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                    {portfolio.map(asset => (
                        <AssetCard
                            key={asset.ticker}
                            asset={asset}
                            onDelete={handleDeleteAsset}
                            currentPrice={prices[asset.ticker]}
                            isLoading={isLoadingPrices}
                        />
                    ))}
                </div>
            ) : (
                <div className="text-center py-16 bg-white dark:bg-gray-800 rounded-lg shadow">
                    <Briefcase size={48} className="mx-auto text-gray-400" />
                    <h2 className="mt-4 text-xl font-semibold text-gray-700 dark:text-gray-200">Sua carteira está vazia</h2>
                    <p className="mt-2 text-gray-500 dark:text-gray-400">Comece adicionando sua primeira transação.</p>
                </div>
            )}

            <TransactionModal
                isOpen={isTransactionModalOpen}
                onClose={() => setTransactionModalOpen(false)}
                onSave={handleSaveTransaction}
                assets={portfolio}
            />

            <ImportModal
                isOpen={isImportModalOpen}
                onClose={() => setImportModalOpen(false)}
                onImport={handleImportTransactions}
            />
        </div>
    );
};

export default Investments;