import React from 'react';
import { usePortfolio } from '../context/PortfolioContext';
import PortfolioCharts from '../components/PortfolioCharts';

const Dashboard = () => {
    const { portfolio, prices, financialSummary, rechartsReady, rechartsError } = usePortfolio();

    return (
        <div>
            <h1 className="text-3xl font-bold text-gray-800 dark:text-white mb-6">Painel Principal</h1>
            <PortfolioCharts
                summary={financialSummary}
                assets={portfolio}
                prices={prices}
                rechartsReady={rechartsReady}
                rechartsError={rechartsError}
            />
        </div>
    );
};

export default Dashboard;