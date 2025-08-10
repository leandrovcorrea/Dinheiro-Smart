import React, { useMemo } from 'react';
import MetricCard from './MetricCard';
import { Briefcase, BarChart2, DollarSign, TrendingUp, TrendingDown, PieChart as PieIcon, BrainCircuit, AlertTriangle } from 'lucide-react';

const PortfolioCharts = ({ summary, assets, prices, rechartsReady, rechartsError }) => {
    const { unrealizedProfit, unrealizedLoss, totalInvested, totalCurrentValue } = useMemo(() => {
        let profit = 0, loss = 0, invested = 0, currentValue = 0;
        assets.forEach(asset => {
            const currentPrice = prices[asset.ticker] || asset.avgPrice;
            const assetCurrentValue = asset.quantity * currentPrice;
            const assetTotalCost = asset.quantity * asset.avgPrice;
            const pnl = assetCurrentValue - assetTotalCost;
            if (pnl > 0) profit += pnl; else loss += pnl;
            invested += assetTotalCost;
            currentValue += assetCurrentValue;
        });
        return { unrealizedProfit: profit, unrealizedLoss: loss, totalInvested: invested, totalCurrentValue: currentValue };
    }, [assets, prices]);

    const distributionData = useMemo(() => {
        const dataMap = assets.reduce((acc, asset) => {
            const value = (prices[asset.ticker] || asset.avgPrice) * asset.quantity;
            const type = asset.type || 'Outro';
            if (!acc[type]) acc[type] = { name: type, value: 0 };
            acc[type].value += value;
            return acc;
        }, {});
        return Object.values(dataMap);
    }, [assets, prices]);

    const idealDistributionData = [
        { name: 'Ações', value: 50 },
        { name: 'FIIs', value: 25 },
        { name: 'Renda Fixa', value: 20 },
        { name: 'Ação Estrangeira', value: 5 }
    ];

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#AF19FF'];

    const renderCharts = () => {
        if (rechartsError) {
            return (
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
                    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow flex flex-col items-center justify-center h-[314px] text-center">
                        <AlertTriangle className="text-red-500 mb-2" size={32} />
                        <h4 className="font-semibold text-red-500">Erro ao Carregar Gráficos</h4>
                        <p className="text-sm text-gray-500">Não foi possível carregar a biblioteca de visualização.</p>
                    </div>
                    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow flex items-center justify-center h-[314px]">
                        <p className="text-gray-500">(Gráfico indisponível)</p>
                    </div>
                </div>
            );
        }

        if (!rechartsReady || typeof window.Recharts === 'undefined' || !window.Recharts.PieChart) {
            return (
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
                    {[...Array(2)].map((_, i) => (
                        <div key={i} className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow flex items-center justify-center h-[314px]">
                            <p className="text-gray-500">Carregando gráficos...</p>
                        </div>
                    ))}
                </div>
            );
        }

        const { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } = window.Recharts;
        const CustomTooltip = ({ active, payload }) => {
            if (active && payload?.length) {
                return (
                    <div className="bg-white dark:bg-gray-800 p-2 border rounded-md shadow-lg">
                        <p className="label text-gray-800 dark:text-white">
                            {`${payload[0].name} : R$ ${payload[0].value.toFixed(2)} (${(payload[0].percent * 100).toFixed(2)}%)`}
                        </p>
                    </div>
                );
            }
            return null;
        };

        return (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
                <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
                    <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4 flex items-center">
                        <PieIcon size={20} className="mr-2 text-blue-500" />Distribuição da Carteira
                    </h3>
                    {distributionData.length > 0 ? (
                        <ResponsiveContainer width="100%" height={250}>
                            <PieChart>
                                <Pie data={distributionData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80} label>
                                    {distributionData.map((_, i) => (
                                        <Cell key={`cell-${i}`} fill={COLORS[i % COLORS.length]} />
                                    ))}
                                </Pie>
                                <Tooltip content={<CustomTooltip />} />
                                <Legend />
                            </PieChart>
                        </ResponsiveContainer>
                    ) : (
                        <div className="flex items-center justify-center h-full">
                            <p className="text-gray-500">Sem dados para exibir</p>
                        </div>
                    )}
                </div>
                <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
                    <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4 flex items-center">
                        <BrainCircuit size={20} className="mr-2 text-indigo-500" />Alocação Ideal (Sugestão)
                    </h3>
                    <ResponsiveContainer width="100%" height={250}>
                        <PieChart>
                            <Pie data={idealDistributionData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80} label>
                                {idealDistributionData.map((_, i) => (
                                    <Cell key={`cell-ideal-${i}`} fill={COLORS[i % COLORS.length]} />
                                ))}
                            </Pie>
                            <Tooltip formatter={(v) => `${v}%`} />
                            <Legend />
                        </PieChart>
                    </ResponsiveContainer>
                </div>
            </div>
        );
    };

    return (
        <div className="mt-8">
            <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-4">Resumo Financeiro</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <MetricCard title="Custo da Carteira" value={totalInvested} icon={Briefcase} colorClass="text-blue-500" />
                <MetricCard title="Valor Atual" value={totalCurrentValue} icon={BarChart2} colorClass="text-indigo-500" />
                <MetricCard title="Dividendos Recebidos" value={summary.totalDividends} icon={DollarSign} colorClass="text-cyan-500" />
                <MetricCard title="Lucro Não Realizado" value={unrealizedProfit} icon={TrendingUp} colorClass="text-green-500" />
                <MetricCard title="Lucro Realizado" value={summary.realizedGains} icon={TrendingUp} colorClass="text-green-500" />
                <MetricCard title="Prejuízo Não Realizado" value={Math.abs(unrealizedLoss)} icon={TrendingDown} colorClass="text-red-500" />
                <MetricCard title="Prejuízo Realizado" value={Math.abs(summary.realizedLosses)} icon={TrendingDown} colorClass="text-red-500" />
            </div>
            {renderCharts()}
        </div>
    );
};

export default PortfolioCharts;