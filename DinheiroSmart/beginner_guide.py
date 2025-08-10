import streamlit as st
from ui_components import show_tutorial_step, show_info_message, show_success_message

def show_beginner_tutorial():
    """Tutorial completo para iniciantes"""
    st.markdown("## 🎯 Tutorial para Iniciantes")
    
    st.markdown("""
        <div style="background: #dbeafe; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #1e40af; margin-top: 0;">👋 Bem-vindo ao mundo dos investimentos!</h3>
            <p style="color: #1e40af;">Este tutorial vai te ensinar como usar a plataforma passo a passo, mesmo se você nunca investiu antes.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Seletor de etapas
    etapa = st.selectbox(
        "Escolha por onde começar:",
        [
            "1️⃣ O que é análise de ações?",
            "2️⃣ Como analisar minha primeira ação",
            "3️⃣ Como criar minha carteira",
            "4️⃣ Como acompanhar meus investimentos",
            "5️⃣ Entendendo os indicadores básicos"
        ]
    )
    
    if "1️⃣" in etapa:
        show_what_is_analysis()
    elif "2️⃣" in etapa:
        show_first_analysis()
    elif "3️⃣" in etapa:
        show_create_portfolio()
    elif "4️⃣" in etapa:
        show_track_investments()
    elif "5️⃣" in etapa:
        show_basic_indicators()

def show_what_is_analysis():
    """Explica o que é análise de ações"""
    show_tutorial_step(
        1, 
        "O que é análise de ações?", 
        "Análise de ações é como 'investigar' uma empresa antes de comprar suas ações. É como pesquisar antes de comprar um carro!"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            ### 🔍 O que analisamos?
            - **Preço da ação**: Está cara ou barata?
            - **Lucros da empresa**: Ela ganha dinheiro?
            - **Dividendos**: Ela paga "mesada" aos acionistas?
            - **Crescimento**: Está crescendo ou diminuindo?
        """)
    
    with col2:
        st.markdown("""
            ### 🎯 Por que analisar?
            - Evitar comprar ações muito caras
            - Encontrar boas oportunidades
            - Investir com mais segurança
            - Entender o que você está comprando
        """)
    
    show_info_message("Dica: Comece sempre analisando empresas que você conhece, como bancos, supermercados ou empresas de telefonia!")

def show_first_analysis():
    """Tutorial para primeira análise"""
    show_tutorial_step(
        2, 
        "Sua primeira análise", 
        "Vamos analisar uma ação juntos! Siga os passos abaixo:"
    )
    
    st.markdown("### 📋 Passo a passo:")
    
    with st.expander("🔸 Passo 1: Escolher uma ação"):
        st.markdown("""
        1. Vá para a aba **"📊 Analisar Ações"**
        2. Digite o código da ação (ex: PETR4, VALE3, ITUB4)
        3. Clique em "Analisar"
        
        **Dica**: Se não souber códigos, comece com:
        - PETR4 (Petrobras)
        - VALE3 (Vale)
        - ITUB4 (Itaú)
        """)
    
    with st.expander("🔸 Passo 2: Entender os resultados"):
        st.markdown("""
        Após a análise, você verá:
        - **Preço Atual**: Quanto custa a ação hoje
        - **Preço Justo**: Quanto a ação deveria custar
        - **Recomendação**: Se é uma boa compra ou não
        - **Indicadores**: Números que mostram a saúde da empresa
        """)
    
    with st.expander("🔸 Passo 3: Tomar a decisão"):
        st.markdown("""
        - **Verde** = Ação pode estar barata (boa oportunidade)
        - **Amarelo** = Ação está no preço justo (neutro)
        - **Vermelho** = Ação pode estar cara (cuidado)
        
        **Importante**: Sempre faça sua própria pesquisa antes de investir!
        """)

def show_create_portfolio():
    """Tutorial para criar carteira"""
    show_tutorial_step(
        3, 
        "Criando sua carteira", 
        "Sua carteira é onde você registra todos os seus investimentos. É como um 'caderninho' digital!"
    )
    
    st.markdown("### 💼 Como funciona:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### ➕ Adicionar investimentos:
        1. Vá para **"💼 Meus Investimentos"**
        2. Clique em "Adicionar Transação"
        3. Preencha:
           - Código da ação (ex: PETR4)
           - Quantidade comprada
           - Preço que pagou
           - Data da compra
        4. Clique em "Salvar"
        """)
    
    with col2:
        st.markdown("""
        #### 📊 O que você verá:
        - Quanto investiu no total
        - Quanto vale hoje
        - Seu lucro ou prejuízo
        - Dividendos recebidos
        - Gráfico da evolução
        """)
    
    show_success_message("Registre todas as suas compras para ter controle total dos seus investimentos!")

def show_track_investments():
    """Tutorial para acompanhar investimentos"""
    show_tutorial_step(
        4, 
        "Acompanhando seus investimentos", 
        "Depois de registrar suas ações, você pode acompanhar como estão se saindo!"
    )
    
    st.markdown("### 📈 Principais telas:")
    
    with st.expander("🏠 Painel Principal (Dashboard)"):
        st.markdown("""
        Aqui você vê o resumo geral:
        - **Valor total** da sua carteira
        - **Lucro/Prejuízo** atual
        - **Gráfico** da evolução
        - **Comparação** com índices como Ibovespa
        """)
    
    with st.expander("👁️ Lista de Acompanhamento"):
        st.markdown("""
        Para ações que você tem interesse mas ainda não comprou:
        - Adicione ações para "vigiar"
        - Veja notícias sobre elas
        - Analise quando quiser
        """)
    
    with st.expander("💰 Meus Dividendos"):
        st.markdown("""
        Acompanhe os dividendos (dinheiro que as empresas pagam):
        - Registre dividendos recebidos
        - Veja o histórico
        - Calcule o rendimento
        """)

def show_basic_indicators():
    """Explica indicadores básicos"""
    show_tutorial_step(
        5, 
        "Indicadores básicos", 
        "Indicadores são 'notas' que ajudam a avaliar se uma empresa é boa ou ruim para investir."
    )
    
    st.markdown("### 📊 Principais indicadores (simplificado):")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 💰 P/L (Preço/Lucro)
        - **O que é**: Quantos anos a empresa levaria para "pagar" o preço da ação
        - **Bom**: Entre 10 e 20
        - **Ruim**: Muito alto (acima de 25) ou negativo
        
        #### 📈 P/VP (Preço/Valor Patrimonial)
        - **O que é**: Se a ação está cara comparada ao patrimônio da empresa
        - **Bom**: Abaixo de 2
        - **Ruim**: Muito alto (acima de 3)
        """)
    
    with col2:
        st.markdown("""
        #### 💵 Dividend Yield
        - **O que é**: Quanto % a empresa paga de dividendos por ano
        - **Bom**: Acima de 4%
        - **Ótimo**: Acima de 6%
        
        #### 🏆 ROE (Retorno sobre Patrimônio)
        - **O que é**: Quão eficiente a empresa é em gerar lucro
        - **Bom**: Acima de 15%
        - **Ótimo**: Acima de 20%
        """)
    
    st.markdown("""
    ---
    ### 🎯 Dica de Ouro:
    **Não se baseie em apenas um indicador!** Use vários juntos para ter uma visão completa da empresa.
    É como avaliar um carro: você olha o preço, o estado, o consumo, a marca, etc.
    """)
    
    show_info_message("Lembre-se: estes são apenas guias! Cada setor tem suas particularidades.")

def show_common_mistakes():
    """Mostra erros comuns de iniciantes"""
    st.markdown("## ⚠️ Erros Comuns de Iniciantes")
    
    mistakes = [
        {
            "erro": "Investir todo dinheiro em uma só ação",
            "solucao": "Diversifique! Compre ações de diferentes empresas e setores",
            "icon": "🥚"
        },
        {
            "erro": "Comprar ação só porque está subindo",
            "solucao": "Analise a empresa primeiro. Preço subindo não significa boa empresa",
            "icon": "📈"
        },
        {
            "erro": "Vender no desespero quando cai",
            "solucao": "Mantenha a calma. Se a empresa é boa, quedas podem ser oportunidades",
            "icon": "😰"
        },
        {
            "erro": "Não acompanhar os investimentos",
            "solucao": "Use nossa plataforma para monitorar regularmente sua carteira",
            "icon": "👁️"
        }
    ]
    
    for mistake in mistakes:
        st.markdown(f"""
        <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #ef4444;">
            <h4 style="color: #dc2626; margin-top: 0;">{mistake['icon']} {mistake['erro']}</h4>
            <p style="color: #dc2626; margin-bottom: 0;"><strong>Solução:</strong> {mistake['solucao']}</p>
        </div>
        """, unsafe_allow_html=True)