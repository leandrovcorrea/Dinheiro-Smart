import React from 'react';

const Dashboard = () => {
  const cards = [
    { title: 'Saldo Total', value: 'R$ 12.450,00' },
    { title: 'Investimentos Ativos', value: 'R$ 8.320,00' },
    { title: 'Rentabilidade Mensal', value: '+4,2%' },
  ];

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6 text-gray-800 dark:text-white">Painel Principal</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {cards.map(({ title, value }) => (
          <div key={title} className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
            <h2 className="text-sm font-semibold text-gray-500 dark:text-gray-400">{title}</h2>
            <p className="text-2xl font-bold text-gray-900 dark:text-white mt-2">{value}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;