import React, { useState } from 'react';
import { X } from 'lucide-react';

const ImportModal = ({ isOpen, onClose, onImport }) => {
    const [fileContent, setFileContent] = useState(null);
    const [error, setError] = useState('');

    if (!isOpen) return null;

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file && file.type === "text/csv") {
            const reader = new FileReader();
            reader.onload = (e) => {
                setFileContent(e.target.result);
                setError('');
            };
            reader.readAsText(file);
        } else {
            setError("Por favor, selecione um arquivo .csv válido.");
            setFileContent(null);
        }
    };

    const handleImport = () => {
        if (!fileContent) {
            setError("Nenhum arquivo selecionado.");
            return;
        }
        try {
            const lines = fileContent.split('\n').filter(line => line.trim() !== '');
            const headers = lines.shift().toLowerCase().split(',').map(h => h.trim());
            const requiredHeaders = ['tipo', 'data', 'ticker', 'quantidade', 'preco'];
            if (requiredHeaders.some(h => !headers.includes(h))) throw new Error(`Cabeçalhos em falta. Use: ${requiredHeaders.join(', ')}`);

            const transactions = lines.map(line => {
                const values = line.split(',');
                const data = headers.reduce((obj, h, i) => ({ ...obj, [h]: values[i].trim() }), {});
                const type = data.tipo.charAt(0).toUpperCase() + data.tipo.slice(1).toLowerCase();
                if (!['Compra', 'Venda', 'Dividendo'].includes(type)) throw new Error(`Tipo inválido: ${type}`);
                return {
                    id: crypto.randomUUID(),
                    ticker: data.ticker.toUpperCase(),
                    quantity: type !== 'Dividendo' ? parseInt(data.quantidade, 10) : 0,
                    price: parseFloat(data.preco),
                    date: data.data,
                    type: type,
                    assetInfo: { type: 'Ação', country: 'Brasil' }
                };
            });
            onImport(transactions);
            onClose();
        } catch (e) {
            setError(`Erro ao processar: ${e.message}`);
        }
    };

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
            <div className="bg-white dark:bg-gray-800 rounded-lg p-8 w-full max-w-lg m-4">
                <div className="flex justify-between items-center mb-6">
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Importar Transações</h2>
                    <button onClick={onClose} className="text-gray-500 hover:text-gray-800 dark:hover:text-white"><X size={24} /></button>
                </div>
                <div className="space-y-4">
                    <div>
                        <p className="text-sm text-gray-600 dark:text-gray-300">Selecione um arquivo CSV com as colunas:</p>
                        <code className="text-xs bg-gray-100 dark:bg-gray-900 p-2 rounded-md block my-2">tipo,data,ticker,quantidade,preco</code>
                        <ul className="text-xs list-disc list-inside text-gray-500 dark:text-gray-400">
                            <li><b>tipo:</b> Compra, Venda ou Dividendo</li>
                            <li><b>data:</b> formato AAAA-MM-DD</li>
                            <li><b>quantidade:</b> (deixar em branco para dividendos)</li>
                            <li><b>preco:</b> preço unitário ou valor total do dividendo</li>
                        </ul>
                    </div>
                    <input type="file" accept=".csv" onChange={handleFileChange}
                        className="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100" />
                    {error && <p className="text-sm text-red-500">{error}</p>}
                    {fileContent && <p className="text-sm text-green-500">Arquivo carregado com sucesso.</p>}
                </div>
                <div className="mt-8 flex justify-end space-x-4">
                    <button type="button" onClick={onClose}
                        className="px-4 py-2 rounded-md text-gray-700 dark:text-gray-200 bg-gray-200 dark:bg-gray-600 hover:bg-gray-300 dark:hover:bg-gray-500">Cancelar</button>
                    <button type="button" onClick={handleImport} disabled={!fileContent}
                        className="px-4 py-2 rounded-md text-white bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400">Importar</button>
                </div>
            </div>
        </div>
    );
};

export default ImportModal;