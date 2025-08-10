import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

class MLPenaltyCalculator:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def _calculate_technical_indicators(self, df):
        """Calcula indicadores técnicos para features do modelo"""
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # Médias móveis
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        
        # Volatilidade
        df['Volatility'] = df['Close'].rolling(window=20).std()
        
        # Volume médio
        df['Volume_MA'] = df['Volume'].rolling(window=20).mean()
        
        return df
    
    def _prepare_features(self, df):
        """Prepara features para o modelo"""
        df = self._calculate_technical_indicators(df)
        
        features = []
        for i in range(20, len(df) - 5):  # 5 dias para frente como target
            row_features = [
                df['RSI'].iloc[i],
                df['SMA_20'].iloc[i] / df['Close'].iloc[i],  # Razão SMA20/Close
                df['SMA_50'].iloc[i] / df['Close'].iloc[i],  # Razão SMA50/Close
                df['Volatility'].iloc[i] / df['Close'].iloc[i],  # Volatilidade normalizada
                df['Volume'].iloc[i] / df['Volume_MA'].iloc[i],  # Volume relativo
                (df['Close'].iloc[i] - df['Close'].iloc[i-5]) / df['Close'].iloc[i-5],  # Retorno 5 dias
                (df['Close'].iloc[i] - df['Close'].iloc[i-20]) / df['Close'].iloc[i-20],  # Retorno 20 dias
            ]
            
            # Target: retorno futuro de 5 dias
            future_return = (df['Close'].iloc[i+5] - df['Close'].iloc[i]) / df['Close'].iloc[i]
            
            if not any(pd.isna(row_features)) and not pd.isna(future_return):
                features.append(row_features + [future_return])
        
        return np.array(features)
    
    def train_model(self, tickers=['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA']):
        """Treina o modelo com dados históricos de múltiplas ações"""
        all_features = []
        
        for ticker in tickers:
            try:
                stock = yf.Ticker(ticker)
                df = stock.history(period='2y')
                if len(df) > 100:
                    features = self._prepare_features(df)
                    if len(features) > 0:
                        all_features.append(features)
            except:
                continue
        
        if not all_features:
            return False
            
        # Combina dados de todas as ações
        combined_features = np.vstack(all_features)
        X = combined_features[:, :-1]  # Features
        y = combined_features[:, -1]   # Target (retorno futuro)
        
        # Treina o modelo
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        
        return True
    
    def predict_performance_probability(self, ticker):
        """Prediz a probabilidade de performance positiva de uma ação"""
        if not self.is_trained:
            if not self.train_model():
                return 0.5  # Neutro se não conseguir treinar
        
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period='3mo')
            
            if len(df) < 50:
                return 0.5
            
            df = self._calculate_technical_indicators(df)
            
            # Pega as features mais recentes
            latest_features = [
                df['RSI'].iloc[-1],
                df['SMA_20'].iloc[-1] / df['Close'].iloc[-1],
                df['SMA_50'].iloc[-1] / df['Close'].iloc[-1],
                df['Volatility'].iloc[-1] / df['Close'].iloc[-1],
                df['Volume'].iloc[-1] / df['Volume_MA'].iloc[-1],
                (df['Close'].iloc[-1] - df['Close'].iloc[-6]) / df['Close'].iloc[-6],
                (df['Close'].iloc[-1] - df['Close'].iloc[-21]) / df['Close'].iloc[-21],
            ]
            
            if any(pd.isna(latest_features)):
                return 0.5
            
            # Faz a predição
            X_scaled = self.scaler.transform([latest_features])
            predicted_return = self.model.predict(X_scaled)[0]
            
            # Converte retorno em probabilidade (sigmoid)
            probability = 1 / (1 + np.exp(-predicted_return * 10))
            
            return max(0.1, min(0.9, probability))  # Limita entre 0.1 e 0.9
            
        except:
            return 0.5
    
    def calculate_ml_penalty(self, ticker, base_penalty=0.1):
        """Calcula penalidade baseada em ML"""
        prob = self.predict_performance_probability(ticker)
        
        # Penalidade inversamente proporcional à probabilidade
        # Probabilidade alta = penalidade baixa
        # Probabilidade baixa = penalidade alta
        penalty = base_penalty * (2 - 2 * prob)
        
        return max(0.01, min(0.5, penalty))  # Limita entre 1% e 50%

# Instância global do calculador
ml_calculator = MLPenaltyCalculator()