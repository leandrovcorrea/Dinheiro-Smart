import React from 'react';
import { Trash2 } from 'lucide-react';

const AssetCard = ({ asset, onDelete, currentPrice, isLoading }) => {
    const priceToUse = currentPrice || asset.avgPrice;
    const hasRealPrice = currentPrice !== null && currentPrice !== undefined;
    const currentValue = asset.quantity * priceToUse;
    const totalCost = asset.quantity * asset.avgPrice;
    const pnl = currentValue - totalCost;
    const pnlPercent = totalCost > 0 ? (pnl / totalCost) * 100 : 0;
    const pnlColor = pnl > 0.005 ? 'text-green-500' : pnl < -0.005 ? 'text-red-500' : 'text-gray-500';

    return (
        <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 flex flex-col justify-between">
            <div>
                <div className="flex justify-between items-start">
                    <h3 className="text-xl font-bold text-gray-800 dark:text-white">{asset.ticker}</h3>
                    <span className={`px-2 py-1 text-xs font-semibold text-white rounded-full ${
                        asset.type === 'Ação' ? 'bg-blue-500' :
                        asset.type === 'FII' ? 'bg-green-500' :
                        asset.type === 'Renda Fixa' ? 'bg-indigo-500' : 'bg-yellow-500'
                    }`}>
                        {asset.type}
                    </span>
                </div>
                <p className="text-sm text-gray-500 dark:text-gray-400">{asset.name || 'Nome do Ativo'}</p>
                <div className="mt-4 space-y-2 text-sm">
                    <div className="flex justify-between">
                        <span className="text-gray-600 dark:text-gray-300">Quantidade:</span>
                        <span className="font-medium text-gray-800 dark:text-white">{asset.quantity}</span>
                    </div>
                    <div className="flex justify-between">
                        <span className="text-gray-600 dark:text-gray-300">Preço Médio:</span>
                        <span className="font-medium text-gray-800 dark:text-white">R$ {parseFloat(asset.avgPrice).toFixed(2)}</span>
                    </div>
                    <div className="flex justify-between">
                        <span className="text-gray-600 dark:text-gray-300">Custo Total:</span>
                        <span className="font-medium text-gray-800 dark:text-white">R$ {totalCost.toFixed(2)}</span>
                    </div>
                    <div className="mt-2 pt-2 border-t border-gray-200 dark:border-gray-700">
                        <div className="flex justify-between items-center">
                            <span className="text-gray-600 dark:text-gray-300">Cotação Atual:</span>
                            {isLoading ? (
                                <span className="text-sm text-gray-500 animate-pulse">A carregar...</span>
                            ) : (
                                <span className={`font-medium ${!hasRealPrice ? 'text-yellow-500' : 'text-gray-800 dark:text-white'}`}>
                                    {!hasRealPrice ? `N/D` : `R$ ${priceToUse.toFixed(2)}`}
                                </span>
                            )}
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600 dark:text-gray-300">Valor Atual:</span>
                            <span className="font-medium text-gray-800 dark:text-white">R$ {currentValue.toFixed(2)}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600 dark:text-gray-300">Resultado:</span>
                            <span className={`font-bold ${pnlColor}`}>
                                {pnl.toFixed(2)} ({pnlPercent.toFixed(2)}%)
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <div className="flex justify-end items-center mt-4 pt-4 border-t border-gray-200 dark:border-gray-700 space-x-2">
                <button onClick={() => onDelete(asset.ticker)} className="p-2 text-gray-500 hover:text-red-500 transition-colors duration-200" title="Excluir todo o histórico deste ativo">
                    <Trash2 size={18} />
                </button>
            </div>
        </div>
    );
};

export default AssetCard;