import streamlit as st
import pandas as pd
import plotly.express as px
import re

def render_analise_carteira():
    """Widget de análise de carteira para integrar em qualquer app"""
    
    # Funções auxiliares
    def limpar(valor):
        if pd.isnull(valor): return None
        valor = str(valor).strip().replace('.', '').replace(',', '.')
        valor = re.sub(r'[^\d\.\-]', '', valor)
        try: return float(valor)
        except: return None
    
    def avaliar_acao(row, tickers_rj):
        if row['TICKER'] in tickers_rj: return "🔴 Vender (RJ)"
        pontos, avaliacoes = 0, 0
        criterios = {
            'ROE': lambda v: v < 5,
            'MARG. LIQUIDA': lambda v: v < 5,
            'DIVIDA LIQUIDA / EBIT': lambda v: v > 6,
            'CAGR LUCROS 5 ANOS': lambda v: v < 0,
            'LIQUIDEZ MEDIA DIARIA': lambda v: v < 1000,
            'LPA': lambda v: v < 1,
            'PEG Ratio': lambda v: v > 2
        }
        for campo, regra in criterios.items():
            v = row.get(campo)
            if v is not None:
                avaliacoes += 1
                if regra(v): pontos += 1
        if avaliacoes == 0: return "⚪ Dados insuficientes"
        elif pontos >= 4: return "🔴 Vender"
        elif pontos >= 2: return "🟡 Avaliar"
        else: return "🟢 Manter"
    
    def avaliar_fii(row, tickers_rj):
        if row['TICKER'] in tickers_rj: return "🔴 Vender (RJ)"
        pontos, avaliacoes = 0, 0
        criterios = {
            'DY': lambda v: v < 1.5,
            'LIQUIDEZ MEDIA DIARIA': lambda v: v < 1000,
            'P/VP': lambda v: v < 0.7 or v > 1.4,
            'CAGR DIVIDENDOS 3 ANOS': lambda v: v < -5
        }
        for campo, regra in criterios.items():
            v = row.get(campo)
            if v is not None:
                avaliacoes += 1
                if regra(v): pontos += 1
        if avaliacoes == 0: return "⚪ Dados insuficientes"
        elif pontos >= 3: return "🔴 Vender"
        elif pontos == 2: return "🟡 Avaliar"
        else: return "🟢 Manter"
    
    def gerar_alerta(row, tickers_rj):
        if row.get('TICKER') in tickers_rj: return "🟥 Em RJ"
        if row.get('DIVIDA LIQUIDA / EBIT') and row['DIVIDA LIQUIDA / EBIT'] > 6:
            return "🔴 Endividamento elevado"
        if row.get('ROE') and row['ROE'] > 20:
            return "🟢 Alta rentabilidade"
        if row.get('PEG Ratio') and row['PEG Ratio'] < 0.5:
            return "🟢 Crescimento barato"
        return "⚪ Sem alerta"
    
    # Empresas em RJ (lista conhecida)
    tickers_rj = ['OIBR3', 'OIBR4', 'LAME3', 'LAME4', 'RECV3', 'GOLL4']
    
    try:
        # Carregar dados
        df_acao = pd.read_csv("statusinvest-busca-avancada (1).csv", sep=';', dtype=str)
        df_fii = pd.read_csv("statusinvest-busca-avancada (2).csv", sep=';', dtype=str)
        
        # Limpar nomes das colunas
        df_acao.columns = [col.strip() for col in df_acao.columns]
        df_fii.columns = [col.strip() for col in df_fii.columns]
        
        # Limpeza de dados
        colunas_numericas_acao = ['ROE', 'MARG. LIQUIDA', 'DIVIDA LIQUIDA / EBIT', 'CAGR LUCROS 5 ANOS',
                                 'LIQUIDEZ MEDIA DIARIA', 'LPA', 'PEG Ratio', 'PRECO']
        colunas_numericas_fii = ['DY', 'LIQUIDEZ MEDIA DIARIA', 'P/VP', 'CAGR DIVIDENDOS 3 ANOS', 'PRECO']
        
        for col in colunas_numericas_acao:
            if col in df_acao.columns:
                df_acao[col] = df_acao[col].apply(limpar)
        
        for col in colunas_numericas_fii:
            if col in df_fii.columns:
                df_fii[col] = df_fii[col].apply(limpar)
        
        # Aplicar análises
        df_acao['Categoria'] = 'Ação'
        df_fii['Categoria'] = 'FII'
        df_acao['Recomendacao'] = df_acao.apply(lambda row: avaliar_acao(row, tickers_rj), axis=1)
        df_fii['Recomendacao'] = df_fii.apply(lambda row: avaliar_fii(row, tickers_rj), axis=1)
        df_acao['Alerta'] = df_acao.apply(lambda row: gerar_alerta(row, tickers_rj), axis=1)
        df_fii['Alerta'] = df_fii.apply(lambda row: gerar_alerta(row, tickers_rj), axis=1)
        
        # Combinar dados
        df_total = pd.concat([df_acao, df_fii])
        
        # Interface
        st.header("📊 Análise de Carteira")
        
        # Métricas rápidas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Ações", len(df_acao))
        with col2:
            st.metric("Total FIIs", len(df_fii))
        with col3:
            alertas = len(df_total[df_total['Alerta'] != "⚪ Sem alerta"])
            st.metric("Alertas", alertas)
        with col4:
            rj_count = len(df_total[df_total['Alerta'] == "🟥 Em RJ"])
            st.metric("Em RJ", rj_count)
        
        # Abas
        aba1, aba2, aba3 = st.tabs(["📑 Ações", "🏢 FIIs", "🚨 Alertas"])
        
        with aba1:
            st.dataframe(df_acao, use_container_width=True)
            fig1 = px.histogram(df_acao, x="Recomendacao", title="Distribuição - Ações")
            st.plotly_chart(fig1, use_container_width=True)
        
        with aba2:
            st.dataframe(df_fii, use_container_width=True)
            fig2 = px.histogram(df_fii, x="Recomendacao", title="Distribuição - FIIs")
            st.plotly_chart(fig2, use_container_width=True)
        
        with aba3:
            # Filtros de alerta
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if st.button("📋 Todos"):
                    st.session_state.filtro_carteira = "Todos"
            with col2:
                if st.button("🟥 Em RJ"):
                    st.session_state.filtro_carteira = "🟥 Em RJ"
            with col3:
                if st.button("🔴 Endividamento"):
                    st.session_state.filtro_carteira = "🔴 Endividamento elevado"
            with col4:
                if st.button("🟢 Rentabilidade"):
                    st.session_state.filtro_carteira = "🟢 Alta rentabilidade"
            
            # Inicializar filtro
            if 'filtro_carteira' not in st.session_state:
                st.session_state.filtro_carteira = "Todos"
            
            # Aplicar filtro
            if st.session_state.filtro_carteira == "Todos":
                df_filtrado = df_total[df_total['Alerta'] != "⚪ Sem alerta"].copy()
            else:
                df_filtrado = df_total[df_total['Alerta'] == st.session_state.filtro_carteira].copy()
            
            st.subheader(f"📋 {st.session_state.filtro_carteira} ({len(df_filtrado)} ativos)")
            
            if len(df_filtrado) > 0:
                colunas_exibir = ['TICKER', 'Categoria', 'Recomendacao', 'Alerta', 'PRECO']
                colunas_exibir = [col for col in colunas_exibir if col in df_filtrado.columns]
                st.dataframe(df_filtrado[colunas_exibir], use_container_width=True)
            else:
                st.info("Nenhum ativo encontrado")
        
    except FileNotFoundError:
        st.error("❌ Arquivos acoes.csv ou fiis.csv não encontrados!")
    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")

# Para testar o widget independentemente
if __name__ == "__main__":
    st.set_page_config(page_title="Widget Análise Carteira", layout="wide")
    render_analise_carteira()