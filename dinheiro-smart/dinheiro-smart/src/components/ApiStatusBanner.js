import React from 'react';
import { usePortfolio } from '../context/PortfolioContext';

const ApiStatusBanner = () => {
    const { apiStatus } = usePortfolio();

    if (!apiStatus) return null;

    const isError = apiStatus.toLowerCase().includes('erro');
    const bgColor = isError ? 'bg-red-100 dark:bg-red-900' : 'bg-blue-100 dark:bg-blue-900';
    const textColor = isError ? 'text-red-800 dark:text-red-200' : 'text-blue-800 dark:text-blue-200';

    return (
        <div className={`p-2 text-center text-sm ${bgColor} ${textColor}`}>
            {apiStatus}
        </div>
    );
};

export default ApiStatusBanner;