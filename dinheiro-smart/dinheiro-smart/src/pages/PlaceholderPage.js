import React from 'react';

const PlaceholderPage = ({ title }) => (
    <div>
        <h1 className="text-3xl font-bold text-gray-800 dark:text-white mb-6">{title}</h1>
        <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center">
            <h2 className="text-xl font-semibold text-gray-700 dark:text-gray-200">Em Construção</h2>
            <p className="text-gray-500 dark:text-gray-400 mt-2">
                Esta funcionalidade estará disponível em breve.
            </p>
        </div>
    </div>
);

export default PlaceholderPage;