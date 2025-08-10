import streamlit as st

def show_user_guide():
    """Exibe guia do usuário com tutoriais interativos"""
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h1 style='color: white; text-align: center; margin: 0;'>🎯 Guia do Usuário</h1>
        <p style='color: white; text-align: center; margin: 0.5rem 0 0 0;'>Aprenda a usar o Dinheiro $mart em poucos minutos</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tutorial interativo
    tutorial_step = st.selectbox(
        "📚 Escolha o que deseja aprender:",
        [
            "🏠 Como começar",
            "💼 Gerenciar minha carteira",
            "📊 Analisar ações",
            "🎯 Definir alocação ideal",
            "👁️ Usar a watchlist",
            "🔔 Configurar alertas",
            "📈 Entender gráficos"
        ]
    )
    
    if tutorial_step == "🏠 Como começar":
        st.markdown("""
        ### 🚀 Primeiros Passos
        
        **1. Criar sua conta**
        - Clique em "Criar nova conta" na barra lateral
        - Preencha seus dados básicos
        - Faça login com seu e-mail e senha
        
        **2. Navegar pelas abas**
        - 🏠 **Dashboard**: Visão geral da sua carteira
        - 💼 **Minha Carteira**: Adicione suas ações e investimentos
        - 📊 **Análise de Ativos**: Descubra se uma ação está cara ou barata
        - 👁️ **Watchlist**: Acompanhe ações de interesse
        
        **3. Dica importante**
        💡 Comece adicionando algumas ações na sua carteira para ver os gráficos funcionarem!
        """)
        
        if st.button("✅ Entendi! Vamos para o próximo passo", use_container_width=True):
            st.balloons()
    
    elif tutorial_step == "💼 Gerenciar minha carteira":
        st.markdown("""
        ### 💼 Como Adicionar Suas Ações
        
        **Passo a passo simples:**
        
        1. **Vá para a aba "Minha Carteira"**
        2. **Preencha o formulário:**
           - **Tipo**: Compra ou Venda
           - **Ticker**: Nome da ação (ex: PETR4, VALE3)
           - **Quantidade**: Quantas ações você comprou
           - **Preço**: Por quanto pagou por ação
           - **Data**: Quando comprou
        
        3. **Clique em "Adicionar à Carteira"**
        
        **Exemplos práticos:**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("""
            **Exemplo 1: Ação Brasileira**
            - Ticker: ITUB4
            - Quantidade: 100
            - Preço: R$ 25,50
            - Data: 15/01/2024
            """)
        
        with col2:
            st.info("""
            **Exemplo 2: Ação Americana**
            - Ticker: AAPL
            - Quantidade: 10
            - Preço: $150,00
            - Data: 20/01/2024
            """)
        
        st.success("💡 **Dica**: Você pode importar sua carteira via Excel! Procure pela opção 'Importar Carteira via Excel'")
    
    elif tutorial_step == "📊 Analisar ações":
        st.markdown("""
        ### 📊 Como Descobrir se uma Ação está Cara ou Barata
        
        **É muito simples:**
        
        1. **Vá para "Análise de Ativos"**
        2. **Digite o nome da ação** (ex: PETR4, VALE3, AAPL)
        3. **Clique em "Analisar Ação"**
        
        **O que você verá:**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🟢 Sinais Positivos:**
            - Margem de segurança positiva
            - Preço atual abaixo do valor calculado
            - Indicadores fundamentais saudáveis
            """)
        
        with col2:
            st.markdown("""
            **🔴 Sinais de Alerta:**
            - Margem de segurança negativa
            - Preço atual acima do valor justo
            - Indicadores fundamentais ruins
            """)
        
        st.info("""
        **💡 Interpretação Simples:**
        - **Verde/Positivo**: Ação pode estar barata
        - **Vermelho/Negativo**: Ação pode estar cara
        - **Sempre faça sua própria pesquisa antes de investir!**
        """)
    
    elif tutorial_step == "🎯 Definir alocação ideal":
        st.markdown("""
        ### 🎯 Como o Sistema Calcula sua Alocação Ideal
        
        **Funciona automaticamente:**
        
        1. **Vá para "Minha Carteira"**
        2. **Procure por "Alocação Ideal da Carteira"**
        3. **Clique em um dos botões:**
           - 📊 **Redistribuição Básica**: Análise fundamentalista simples
           - 🧠 **Redistribuição por IA**: Análise avançada com inteligência artificial
        
        **O que acontece:**
        - O sistema analisa todas as suas ações
        - Calcula qual % ideal para cada uma
        - Mostra quanto comprar ou vender para rebalancear
        
        **Exemplo prático:**
        """)
        
        st.success("""
        **Sua carteira atual:**
        - ITUB4: 60% (muito concentrado)
        - PETR4: 40%
        
        **Sugestão da IA:**
        - ITUB4: 35% → Vender R$ 2.500
        - PETR4: 45% → Comprar R$ 1.000
        - VALE3: 20% → Comprar R$ 1.500 (nova posição)
        """)
    
    elif tutorial_step == "👁️ Usar a watchlist":
        st.markdown("""
        ### 👁️ Como Acompanhar Ações de Interesse
        
        **Para que serve:**
        - Monitorar ações que você quer comprar
        - Acompanhar preços sem precisar comprar
        - Ver notícias das empresas
        
        **Como usar:**
        1. **Vá para "Watchlist"**
        2. **Digite o ticker da ação** (ex: MGLU3, TSLA)
        3. **Clique em "Adicionar"**
        4. **Acompanhe preços e notícias**
        
        **Funcionalidades:**
        - ✅ Preços atualizados
        - 📰 Notícias recentes
        - 📊 Botão para análise rápida
        - 🗑️ Remover quando não interessar mais
        """)
    
    elif tutorial_step == "🔔 Configurar alertas":
        st.markdown("""
        ### 🔔 Como Receber Alertas de Preço
        
        **Nunca mais perca uma oportunidade:**
        
        1. **Vá para "Minha Carteira"**
        2. **Na seção "Posição Atual e Alertas"**
        3. **Digite o preço desejado** na coluna "Alerta de Preço"
        4. **Clique em "Salvar"**
        
        **Como funciona:**
        - Quando a ação atingir seu preço-alvo
        - Você receberá um e-mail automático
        - O alerta será desativado após o envio
        
        **Exemplo:**
        - PETR4 está a R$ 30,00
        - Você quer comprar a R$ 25,00
        - Configure o alerta para R$ 25,00
        - Receberá e-mail quando atingir esse preço
        """)
    
    elif tutorial_step == "📈 Entender gráficos":
        st.markdown("""
        ### 📈 Como Interpretar os Gráficos
        
        **Dashboard - Evolução do Patrimônio:**
        - **Linha verde subindo**: Sua carteira está valorizando
        - **Linha vermelha descendo**: Sua carteira está desvalorizando
        - **Compare com índices**: Veja se está melhor que o IBOV
        
        **Gráficos de Pizza:**
        - **Distribuição Atual**: Como sua carteira está hoje
        - **Distribuição Ideal**: Como deveria estar (sugestão da IA)
        
        **Análise de Ativos:**
        - **Gráfico de preços**: Histórico da ação
        - **Gráfico de dividendos**: Quanto a empresa paga aos acionistas
        
        **Cores importantes:**
        - 🟢 **Verde**: Positivo, lucro, recomendação de compra
        - 🔴 **Vermelho**: Negativo, prejuízo, recomendação de venda
        - 🟡 **Amarelo/Laranja**: Neutro, atenção
        """)

def show_quick_tips():
    """Dicas rápidas para usuários"""
    st.markdown("""
    ### ⚡ Dicas Rápidas
    
    **🎯 Para Iniciantes:**
    - Comece com ações perenes (Bancos, Energia, Saneamento, Seguros...)
    - Diversifique: não coloque tudo em uma ação só
    - Use a análise automática antes de comprar
    
    **💡 Truques da Ferramenta:**
    - Digite apenas "PETR4" (sem .SA) para ações brasileiras
    - Use a importação Excel para carteiras grandes
    - Configure alertas para não perder oportunidades
    
    **⚠️ Cuidados Importantes:**
    - Esta ferramenta é educativa, não é recomendação de investimento
    - Sempre faça sua própria pesquisa
    - Diversifique seus investimentos
   
    """)

def show_glossary():
    """Glossário de termos financeiros"""
    st.markdown("""
    ### 📖 Glossário - Termos Simples
    
    **Ticker**: Nome da ação na bolsa (ex: PETR4, VALE3)
    
    **P/L**: Preço dividido pelo Lucro. Quanto menor, mais barata a ação
    
    **Dividend Yield**: Quanto a empresa paga de dividendos por ano (em %)
    
    **ROE**: Retorno sobre Patrimônio. Quanto a empresa ganha com o dinheiro dos acionistas
    
    **Margem de Segurança**: Diferença entre preço justo e preço atual
    
    **Alocação**: Quanto % da carteira cada ação representa
    
    **Rebalanceamento**: Ajustar a carteira para a distribuição ideal
    
    **Watchlist**: Lista de ações que você quer acompanhar
    
    **Backtest**: Testar uma estratégia com dados do passado
    """)