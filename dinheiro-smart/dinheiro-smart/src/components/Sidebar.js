import React, { useState } from 'react';
import {
    Home, Briefcase, DollarSign, Percent, Calculator, Eye,
    BarChart2, TestTube2, LineChart, HelpCircle, X
} from 'lucide-react';

const Sidebar = ({ activePage, setActivePage }) => {
    const [isSidebarOpen, setIsSidebarOpen] = useState(true);

    const menuItems = [
        { name: 'Painel Principal', icon: Home },
        { name: 'Meus Investimentos', icon: Briefcase },
        { name: 'Meus Dividendos', icon: DollarSign },
        { name: 'Yield on Cost', icon: Percent },
        { name: 'Calculadora de Aporte', icon: Calculator },
        { name: 'Lista de Acompanhamento', icon: Eye },
        { name: 'Analisar Ações', icon: BarChart2 },
        { name: 'Testar Estratégias', icon: TestTube2 },
        { name: 'Análise do Mercado', icon: LineChart },
        { name: 'Ajuda e Tutorial', icon: HelpCircle },
    ];

    return (
        <aside className={`bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 flex flex-col transition-all duration-300 ${isSidebarOpen ? 'w-64' : 'w-20'}`}>
            <div className={`flex items-center ${isSidebarOpen ? 'justify-between' : 'justify-center'} p-4 h-16 border-b dark:border-gray-700`}>
                {isSidebarOpen && <span className="text-xl font-bold text-gray-800 dark:text-white">Dinheiro$mart</span>}
                <button onClick={() => setIsSidebarOpen(!isSidebarOpen)} className="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700">
                    {isSidebarOpen ? <X size={20} /> : <Home size={20} />}
                </button>
            </div>
            <nav className="flex-1 mt-4 space-y-2">
                {menuItems.map(item => (
                    <a
                        key={item.name}
                        href="#"
                        onClick={(e) => {
                            e.preventDefault();
                            setActivePage(item.name);
                        }}
                        className={`flex items-center py-3 px-4 mx-2 rounded-lg transition-colors duration-200 ${
                            activePage === item.name
                                ? 'bg-blue-100 dark:bg-blue-900/50 text-blue-600 dark:text-blue-300'
                                : 'hover:bg-gray-100 dark:hover:bg-gray-700'
                        }`}
                    >
                        <item.icon size={20} />
                        {isSidebarOpen && <span className="ml-4 font-medium">{item.name}</span>}
                    </a>
                ))}
            </nav>
        </aside>
    );
};

export default Sidebar;