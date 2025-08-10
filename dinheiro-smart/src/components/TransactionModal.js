import React, { useState, useEffect } from 'react';
import { X } from 'lucide-react';

const TransactionModal = ({ isOpen, onClose, onSave, assets }) => {
    const [transactionType, setTransactionType] = useState('Compra');
    const [ticker, setTicker] = useState('');
    const [quantity, setQuantity] = useState('');
    const [price, setPrice] = useState('');
    const [date, setDate] = useState('');
    const [assetType, setAssetType] = useState('Ação');

    useEffect(() => {
        if (isOpen) {
            setDate(new Date().toISOString().split('T')[0]);
            setTicker('');
            setQuantity('');
            setPrice('');
            setTransactionType('Compra');
        }
    }, [isOpen]);

    useEffect(() => {
        const existingAsset = assets.find(a => a.ticker === ticker.toUpperCase());
        if (existingAsset) setAssetType(existingAsset.type);
    }, [ticker, assets]);

    if (!isOpen) return null;

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!ticker || !price || !date || (transactionType !== 'Dividendo' && !quantity)) {
            console.error("Preencha todos os campos obrigatórios.");
            return;
        }
        onSave({
            id: crypto.randomUUID(),
            ticker: ticker.toUpperCase(),
            quantity: transactionType !== 'Dividendo' ? parseInt(quantity, 10) : 0,
            price: parseFloat(price),
            date,
            type: transactionType,
            assetInfo: { type: assetType, country: 'Brasil' }
        });
        onClose();
    };

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
            <div className="bg-white dark:bg-gray-800 rounded-lg p-8 w-full max-w-md m-4">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Adicionar Transação</h2>
                    <button onClick={onClose} className="text-gray-500 hover:text-gray-800 dark:hover:text-white"><X size={24} /></button>
                </div>
                <form onSubmit={handleSubmit}>
                    <div className="space-y-4">
                        <div className="grid grid-cols-3 gap-4">
                            {['Compra', 'Venda', 'Dividendo'].map(type => (
                                <button key={type} type="button" onClick={() => setTransactionType(type)}
                                    className={`w-full py-2 rounded-md text-sm ${transactionType === type ? 'bg-blue-600 text-white' : 'bg-gray-200 dark:bg-gray-700'}`}>
                                    {type}
                                </button>
                            ))}
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Ticker</label>
                            <input type="text" value={ticker} onChange={e => setTicker(e.target.value)}
                                className="w-full px-3 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-gray-800 dark:text-white" placeholder="EX: PETR4, AAPL" />
                        </div>
                        {transactionType === 'Dividendo' ? (
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Valor Total Recebido (R$)</label>
                                <input type="number" step="0.01" value={price} onChange={e => setPrice(e.target.value)}
                                    className="w-full px-3 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-gray-800 dark:text-white" placeholder="150.75" />
                            </div>
                        ) : (
                            <div className="grid grid-cols-2 gap-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Quantidade</label>
                                    <input type="number" value={quantity} onChange={e => setQuantity(e.target.value)}
                                        className="w-full px-3 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-gray-800 dark:text-white" placeholder="100" />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Preço por Unidade (R$)</label>
                                    <input type="number" step="0.01" value={price} onChange={e => setPrice(e.target.value)}
                                        className="w-full px-3 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-gray-800 dark:text-white" placeholder="28.50" />
                                </div>
                            </div>
                        )}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Data</label>
                            <input type="date" value={date} onChange={e => setDate(e.target.value)}
                                className="w-full px-3 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-gray-800 dark:text-white" />
                        </div>
                        {transactionType !== 'Dividendo' && !assets.some(a => a.ticker === ticker.toUpperCase()) && (
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Tipo de Ativo</label>
                                <select value={assetType} onChange={e => setAssetType(e.target.value)}
                                    className="w-full px-3 py-2 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md text-gray-800 dark:text-white">
                                    <option>Ação</option>
                                    <option>FII</option>
                                    <option>Renda Fixa</option>
                                    <option>Ação Estrangeira</option>
                                </select>
                            </div>
                        )}
                    </div>
                    <div className="mt-8 flex justify-end space-x-4">
                        <button type="button" onClick={onClose}
                            className="px-4 py-2 rounded-md text-gray-700 dark:text-gray-200 bg-gray-200 dark:bg-gray-600 hover:bg-gray-300 dark:hover:bg-gray-500">Cancelar</button>
                        <button type="submit"
                            className="px-4 py-2 rounded-md text-white bg-blue-600 hover:bg-blue-700">Salvar Transação</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default TransactionModal;