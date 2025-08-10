import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class StockMLPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
    
    def prepare_features(self, df):
        """Prepara features técnicas para o modelo"""
        df = df.copy()
        
        # Médias móveis
        df['MA_5'] = df['Close'].rolling(5).mean()
        df['MA_20'] = df['Close'].rolling(20).mean()
        df['MA_50'] = df['Close'].rolling(50).mean()
        
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # Volatilidade
        df['Volatility'] = df['Close'].rolling(20).std()
        
        # Volume normalizado
        df['Volume_MA'] = df['Volume'].rolling(20).mean()
        df['Volume_Ratio'] = df['Volume'] / df['Volume_MA']
        
        # Retornos
        df['Return_1d'] = df['Close'].pct_change()
        df['Return_5d'] = df['Close'].pct_change(5)
        df['Return_20d'] = df['Close'].pct_change(20)
        
        # Bollinger Bands
        bb_period = 20
        df['BB_Middle'] = df['Close'].rolling(bb_period).mean()
        bb_std = df['Close'].rolling(bb_period).std()
        df['BB_Upper'] = df['BB_Middle'] + (bb_std * 2)
        df['BB_Lower'] = df['BB_Middle'] - (bb_std * 2)
        df['BB_Position'] = (df['Close'] - df['BB_Lower']) / (df['BB_Upper'] - df['BB_Lower'])
        
        return df
    
    def train_model(self, ticker, period='2y'):
        """Treina o modelo com dados históricos"""
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period=period)
            
            if df.empty:
                return False, "Dados não encontrados"
            
            df = self.prepare_features(df)
            
            # Target: retorno futuro de 5 dias
            df['Target'] = df['Close'].shift(-5).pct_change(5)
            
            # Remove NaN
            df = df.dropna()
            
            if len(df) < 100:
                return False, "Dados insuficientes"
            
            # Features para o modelo
            feature_cols = ['MA_5', 'MA_20', 'MA_50', 'RSI', 'Volatility', 
                           'Volume_Ratio', 'Return_1d', 'Return_5d', 'Return_20d', 'BB_Position']
            
            X = df[feature_cols]
            y = df['Target']
            
            # Split dos dados
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Normalização
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)
            
            # Treino
            self.model.fit(X_train_scaled, y_train)
            
            # Score
            train_score = self.model.score(X_train_scaled, y_train)
            test_score = self.model.score(X_test_scaled, y_test)
            
            self.is_trained = True
            self.feature_cols = feature_cols
            
            return True, {
                'train_score': train_score,
                'test_score': test_score,
                'data_points': len(df)
            }
            
        except Exception as e:
            return False, str(e)
    
    def predict_performance(self, ticker):
        """Faz predição de performance"""
        if not self.is_trained:
            return None, "Modelo não treinado"
        
        try:
            stock = yf.Ticker(ticker)
            df = stock.history(period='3mo')
            
            if df.empty:
                return None, "Dados não encontrados"
            
            df = self.prepare_features(df)
            df = df.dropna()
            
            if len(df) == 0:
                return None, "Dados insuficientes após processamento"
            
            # Última observação
            latest_data = df[self.feature_cols].iloc[-1:].values
            latest_scaled = self.scaler.transform(latest_data)
            
            # Predição
            prediction = self.model.predict(latest_scaled)[0]
            
            # Probabilidade baseada na predição
            if prediction > 0.05:
                prob_up = min(0.8, 0.5 + prediction * 5)
                sentiment = "ALTA"
                color = "green"
            elif prediction < -0.05:
                prob_up = max(0.2, 0.5 + prediction * 5)
                sentiment = "BAIXA"
                color = "red"
            else:
                prob_up = 0.5
                sentiment = "NEUTRO"
                color = "orange"
            
            return {
                'prediction': prediction,
                'probability_up': prob_up,
                'sentiment': sentiment,
                'color': color,
                'current_price': df['Close'].iloc[-1]
            }, None
            
        except Exception as e:
            return None, str(e)

def show_ml_analysis():
    """Interface para análise com ML"""
    st.markdown("## 🤖 Análise com Inteligência Artificial")
    
    st.markdown("""
        <div style="background: #f0f9ff; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #1e40af; margin-top: 0;">🧠 Como funciona nossa IA</h3>
            <p style="color: #1e40af; margin-bottom: 0;">
                Nossa inteligência artificial analisa padrões históricos, indicadores técnicos e volume 
                para prever a probabilidade de alta ou baixa nos próximos 5 dias úteis.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        ticker = st.text_input("Digite o código da ação:", placeholder="Ex: PETR4.SA", max_chars=10)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("🤖 Analisar com IA", type="primary", use_container_width=True)
    
    if analyze_btn and ticker:
        with st.spinner("🔄 Treinando modelo e fazendo predição..."):
            predictor = StockMLPredictor()
            
            # Treinar modelo
            success, result = predictor.train_model(ticker)
            
            if success:
                st.success(f"✅ Modelo treinado com {result['data_points']} pontos de dados")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Precisão Treino", f"{result['train_score']:.1%}")
                with col2:
                    st.metric("Precisão Teste", f"{result['test_score']:.1%}")
                
                # Fazer predição
                prediction, error = predictor.predict_performance(ticker)
                
                if prediction:
                    st.markdown("---")
                    st.markdown("### 🎯 Predição da IA")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown(f"""
                            <div style="text-align: center; padding: 2rem; background: {prediction['color']}20; border-radius: 10px;">
                                <h2 style="color: {prediction['color']}; margin: 0;">{prediction['sentiment']}</h2>
                                <p style="margin: 0.5rem 0 0 0;">Tendência prevista</p>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.metric(
                            "Probabilidade de Alta",
                            f"{prediction['probability_up']:.1%}",
                            delta=f"{prediction['prediction']:.1%}"
                        )
                    
                    with col3:
                        st.metric("Preço Atual", f"R$ {prediction['current_price']:.2f}")
                    
                    # Gráfico de confiança
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = prediction['probability_up'] * 100,
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Confiança da Predição (%)"},
                        gauge = {
                            'axis': {'range': [None, 100]},
                            'bar': {'color': prediction['color']},
                            'steps': [
                                {'range': [0, 30], 'color': "lightgray"},
                                {'range': [30, 70], 'color': "yellow"},
                                {'range': [70, 100], 'color': "lightgreen"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 90
                            }
                        }
                    ))
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Aviso importante
                    st.warning("""
                        ⚠️ **Importante**: Esta é uma predição baseada em padrões históricos e não garante resultados futuros. 
                        Use sempre como uma ferramenta adicional em sua análise, nunca como única base para decisões de investimento.
                    """)
                    
                else:
                    st.error(f"❌ Erro na predição: {error}")
            else:
                st.error(f"❌ Erro no treinamento: {result}")
    
    elif analyze_btn and not ticker:
        st.warning("⚠️ Digite o código de uma ação primeiro!")

def show_ml_portfolio_analysis():
    """Análise ML da carteira completa"""
    st.markdown("### 🎯 Análise IA da Carteira")
    
    # Simulação de carteira para demonstração
    sample_portfolio = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA']
    
    if st.button("🤖 Analisar Carteira com IA"):
        results = []
        progress_bar = st.progress(0)
        
        for i, ticker in enumerate(sample_portfolio):
            with st.spinner(f"Analisando {ticker}..."):
                predictor = StockMLPredictor()
                success, _ = predictor.train_model(ticker)
                
                if success:
                    prediction, _ = predictor.predict_performance(ticker)
                    if prediction:
                        results.append({
                            'Ação': ticker.replace('.SA', ''),
                            'Tendência': prediction['sentiment'],
                            'Prob. Alta': f"{prediction['probability_up']:.1%}",
                            'Predição': f"{prediction['prediction']:.1%}"
                        })
                
                progress_bar.progress((i + 1) / len(sample_portfolio))
        
        if results:
            try:
                # Converter strings de porcentagem para valores numéricos para evitar problemas de tipo
                df_results = pd.DataFrame(results)
                
                # Garantir que todas as colunas têm tipos consistentes
                for col in df_results.columns:
                    if 'Prob' in col or 'Predição' in col:
                        # Manter como string para exibição
                        pass
                    elif df_results[col].dtype == 'object':
                        # Tentar converter para string para garantir tipo consistente
                        df_results[col] = df_results[col].astype(str)
                
                st.dataframe(df_results, use_container_width=True)
            except Exception as e:
                st.error(f"Erro ao exibir resultados: {e}")
                # Exibir de forma alternativa
                for result in results:
                    st.write(f"{result['Ação']}: {result['Tendência']} - {result['Prob. Alta']}")
                    st.write("---")
            
            # Resumo
            high_prob = len([r for r in results if float(r['Prob. Alta'].replace('%', '')) > 60])
            st.info(f"📊 Resumo: {high_prob} de {len(results)} ações com alta probabilidade de valorização")