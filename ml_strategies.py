import streamlit as st
import pandas as pd
import numpy as np
from ml_predictor import StockMLPredictor
import plotly.express as px
import plotly.graph_objects as go

def show_ml_backtesting():
    """Backtesting com estratégias baseadas em ML"""
    st.markdown("## 🧪 Backtesting com Inteligência Artificial")
    
    st.markdown("""
        <div style="background: #f0fdf4; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #166534; margin-top: 0;">🎯 Estratégia IA</h3>
            <p style="color: #166534; margin-bottom: 0;">
                Teste uma estratégia que compra quando a IA prevê alta probabilidade de valorização 
                e vende quando prevê baixa probabilidade.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ticker = st.text_input("Ação para testar:", value="PETR4.SA")
    
    with col2:
        threshold_buy = st.slider("Limite para compra (%)", 60, 90, 70)
    
    with col3:
        threshold_sell = st.slider("Limite para venda (%)", 10, 40, 30)
    
    if st.button("🚀 Executar Backtest IA"):
        with st.spinner("Executando backtest com IA..."):
            results = run_ml_backtest(ticker, threshold_buy/100, threshold_sell/100)
            
            if results:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Retorno Total", f"{results['total_return']:.1%}")
                
                with col2:
                    st.metric("Número de Trades", results['num_trades'])
                
                with col3:
                    st.metric("Taxa de Acerto", f"{results['win_rate']:.1%}")
                
                # Gráfico de performance
                try:
                    # Garantir que todas as colunas numéricas são do mesmo tipo
                    df_plot = results['portfolio_df'].copy()
                    for col in df_plot.columns:
                        if col != 'Data' and pd.api.types.is_numeric_dtype(df_plot[col]):
                            df_plot[col] = df_plot[col].astype(float)
                    
                    fig = px.line(df_plot, x='Data',
                                y=['Valor Carteira', 'Buy & Hold'],
                                title="Performance da Estratégia IA vs Buy & Hold")
                    st.plotly_chart(fig, use_container_width=True)
                except Exception as e:
                    st.error(f"Erro ao gerar gráfico: {e}")
                    # Alternativa simples caso o gráfico falhe
                    st.line_chart(results['portfolio_df'][['Valor Carteira', 'Buy & Hold']])
                
                # Detalhes dos trades
                if results['trades']:
                    st.subheader("📋 Histórico de Trades")
                    trades_df = pd.DataFrame(results['trades'])
                    st.dataframe(trades_df, use_container_width=True)

def run_ml_backtest(ticker, buy_threshold, sell_threshold):
    """Executa backtest com estratégia baseada em ML"""
    try:
        # Simulação simplificada para demonstração
        dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='W')
        
        # Simular predições da IA
        np.random.seed(42)
        predictions = np.random.uniform(0.2, 0.8, len(dates))
        prices = 100 + np.cumsum(np.random.normal(0, 2, len(dates)))
        
        portfolio_value = 10000
        position = 0
        trades = []
        portfolio_history = []
        
        for i, (date, pred, price) in enumerate(zip(dates, predictions, prices)):
            # Lógica de trading baseada na predição da IA
            if pred > buy_threshold and position == 0:
                # Comprar
                position = portfolio_value / price
                trades.append({
                    'Data': date,
                    'Ação': 'Compra',
                    'Preço': price,
                    'Predição IA': f"{pred:.1%}",
                    'Quantidade': position
                })
                portfolio_value = 0
            
            elif pred < sell_threshold and position > 0:
                # Vender
                portfolio_value = position * price
                trades.append({
                    'Data': date,
                    'Ação': 'Venda',
                    'Preço': price,
                    'Predição IA': f"{pred:.1%}",
                    'Resultado': f"R$ {portfolio_value - 10000:.2f}"
                })
                position = 0
            
            # Valor atual da carteira
            current_value = portfolio_value if position == 0 else position * price
            portfolio_history.append({
                'Data': date,
                'Valor Carteira': float(current_value),  # Garantir tipo float
                'Preço Ação': float(price),              # Garantir tipo float
                'Buy & Hold': float(10000 * (price / prices[0]))  # Garantir tipo float
            })
        
        portfolio_df = pd.DataFrame(portfolio_history)
        
        # Calcular métricas
        final_value = portfolio_df['Valor Carteira'].iloc[-1]
        total_return = (final_value - 10000) / 10000
        
        winning_trades = len([t for t in trades if 'Resultado' in t and float(t['Resultado'].replace('R$ ', '')) > 0])
        total_trades = len([t for t in trades if 'Resultado' in t])
        win_rate = winning_trades / total_trades if total_trades > 0 else 0
        
        return {
            'total_return': total_return,
            'num_trades': len(trades),
            'win_rate': win_rate,
            'trades': trades,
            'portfolio_df': portfolio_df
        }
        
    except Exception as e:
        st.error(f"Erro no backtest: {e}")
        return None

def show_ai_insights():
    """Insights e recomendações da IA"""
    st.markdown("### 🧠 Insights da Inteligência Artificial")
    
    insights = [
        {
            "title": "📈 Tendência de Mercado",
            "content": "Com base na análise de múltiplas ações, o mercado apresenta sinais mistos para os próximos dias.",
            "confidence": 75
        },
        {
            "title": "🎯 Oportunidades Identificadas",
            "content": "Ações do setor bancário mostram padrões favoráveis para valorização.",
            "confidence": 68
        },
        {
            "title": "⚠️ Riscos Detectados",
            "content": "Alta volatilidade prevista para ações de commodities na próxima semana.",
            "confidence": 82
        }
    ]
    
    for insight in insights:
        st.markdown(f"""
            <div style="background: #f8fafc; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #3b82f6;">
                <h4 style="color: #1e40af; margin-top: 0;">{insight['title']}</h4>
                <p style="color: #475569; margin-bottom: 0.5rem;">{insight['content']}</p>
                <div style="background: #e0e7ff; padding: 0.5rem; border-radius: 5px;">
                    <small style="color: #3730a3;">Confiança: {insight['confidence']}%</small>
                </div>
            </div>
        """, unsafe_allow_html=True)