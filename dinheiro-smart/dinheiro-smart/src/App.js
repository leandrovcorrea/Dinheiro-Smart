import React, { useState } from 'react';
import { PortfolioProvider } from './context/PortfolioContext';
import Sidebar from './components/Sidebar';
import ApiStatusBanner from './components/ApiStatusBanner';
import Dashboard from './pages/Dashboard';
import Investments from './pages/Investments';
import PlaceholderPage from './pages/PlaceholderPage';

function App() {
    const [activePage, setActivePage] = useState('Painel Principal');

    const renderContent = () => {
        switch (activePage) {
            case 'Painel Principal': return <Dashboard />;
            case 'Meus Investimentos': return <Investments />;
            default: return <PlaceholderPage title={activePage} />;
        }
    };

    return (
        <PortfolioProvider>
            <div className="flex h-screen bg-gray-100 dark:bg-gray-900 font-sans">
                <Sidebar activePage={activePage} setActivePage={setActivePage} />
                <main className="flex-1 flex flex-col overflow-y-auto">
                    <ApiStatusBanner />
                    <div className="p-6 lg:p-8 flex-1">
                        {renderContent()}
                    </div>
                </main>
            </div>
        </PortfolioProvider>
    );
}

export default App;