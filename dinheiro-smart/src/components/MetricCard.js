import React from 'react';

const MetricCard = ({ title, value, icon, colorClass = 'text-gray-800 dark:text-white', isCurrency = true }) => {
    const Icon = icon;
    return (
        <div className="bg-white dark:bg-gray-800 p-4 rounded-lg shadow">
            <div className="flex items-center">
                <div className={`p-2 bg-gray-200 dark:bg-gray-700 rounded-md mr-4 ${colorClass}`}>
                    <Icon size={20} />
                </div>
                <div>
                    <h3 className="text-sm font-medium text-gray-500 dark:text-gray-400">{title}</h3>
                    <p className={`text-xl font-bold ${colorClass}`}>
                        {isCurrency ? `R$ ${value.toFixed(2)}` : value}
                    </p>
                </div>
            </div>
        </div>
    );
};

export default MetricCard;