import streamlit as st
from ui_components import create_input_with_help, show_success_message, show_warning_message

def simple_stock_analysis_form():
    """Formulário simplificado para análise de ações"""
    st.markdown("### 🔍 Analisar uma Ação - Modo Simples")
    
    st.markdown("""
        <div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="margin: 0; color: #0c4a6e;">
                💡 <strong>Dica:</strong> Digite o código da ação (ex: PETR4, VALE3, ITUB4) e clique em analisar. 
                Vamos mostrar se ela está cara, barata ou no preço justo!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        ticker = create_input_with_help(
            "Código da Ação",
            "Digite o código da ação que você quer analisar (ex: PETR4, VALE3)",
            "text",
            placeholder="Ex: PETR4",
            max_chars=6
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Espaçamento
        analyze_button = st.button("🔍 Analisar Agora", type="primary", use_container_width=True)
    
    if analyze_button and ticker:
        st.session_state.ticker_analisado = ticker.upper()
        show_success_message(f"Analisando {ticker.upper()}... Aguarde!")
        return ticker.upper()
    elif analyze_button and not ticker:
        show_warning_message("Por favor, digite o código de uma ação primeiro!")
    
    return None

def simple_portfolio_form():
    """Formulário simplificado para adicionar investimento"""
    st.markdown("### 💼 Adicionar Investimento - Modo Simples")
    
    st.markdown("""
        <div style="background: #f0fdf4; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="margin: 0; color: #166534;">
                💡 <strong>Como funciona:</strong> Registre aqui todas as ações que você comprou. 
                Assim você pode acompanhar se está ganhando ou perdendo dinheiro!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("add_investment_simple"):
        col1, col2 = st.columns(2)
        
        with col1:
            ticker = create_input_with_help(
                "Código da Ação",
                "Ex: PETR4, VALE3, ITUB4",
                "text",
                placeholder="PETR4"
            )
            
            quantity = create_input_with_help(
                "Quantas ações comprou?",
                "Número de ações que você comprou",
                "number",
                min_value=1,
                value=100
            )
        
        with col2:
            price = create_input_with_help(
                "Por quanto comprou cada ação?",
                "Preço que você pagou por cada ação (em R$)",
                "number",
                min_value=0.01,
                format="%.2f",
                value=10.00
            )
            
            date = create_input_with_help(
                "Quando comprou?",
                "Data da compra",
                "date"
            )
        
        submitted = st.form_submit_button("💾 Salvar Investimento", type="primary", use_container_width=True)
        
        if submitted:
            if ticker and quantity and price and date:
                # Aqui você integraria com a função de salvar da carteira
                show_success_message(f"Investimento em {ticker.upper()} salvo com sucesso!")
                return {
                    'ticker': ticker.upper(),
                    'quantity': quantity,
                    'price': price,
                    'date': date
                }
            else:
                show_warning_message("Por favor, preencha todos os campos!")
    
    return None

def simple_watchlist_form():
    """Formulário simplificado para watchlist"""
    st.markdown("### 👁️ Adicionar à Lista de Acompanhamento")
    
    st.markdown("""
        <div style="background: #fefce8; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="margin: 0; color: #a16207;">
                💡 <strong>Para que serve:</strong> Adicione ações que você tem interesse mas ainda não comprou. 
                Assim você pode acompanhar o preço e as notícias!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        ticker = create_input_with_help(
            "Código da Ação",
            "Ação que você quer acompanhar",
            "text",
            placeholder="Ex: MGLU3"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        add_button = st.button("➕ Adicionar", type="primary", use_container_width=True)
    
    if add_button and ticker:
        show_success_message(f"{ticker.upper()} adicionada à sua lista!")
        return ticker.upper()
    elif add_button and not ticker:
        show_warning_message("Digite o código da ação primeiro!")
    
    return None

def simple_dividend_form():
    """Formulário simplificado para dividendos"""
    st.markdown("### 💰 Registrar Dividendo Recebido")
    
    st.markdown("""
        <div style="background: #ecfdf5; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="margin: 0; color: #065f46;">
                💡 <strong>O que são dividendos:</strong> É dinheiro que as empresas pagam aos acionistas. 
                Como uma "mesada" que você recebe por ter ações da empresa!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("add_dividend_simple"):
        col1, col2 = st.columns(2)
        
        with col1:
            ticker = create_input_with_help(
                "De qual ação?",
                "Código da ação que pagou dividendo",
                "text",
                placeholder="ITUB4"
            )
            
            amount = create_input_with_help(
                "Quanto recebeu?",
                "Valor total recebido em R$",
                "number",
                min_value=0.01,
                format="%.2f",
                value=50.00
            )
        
        with col2:
            date = create_input_with_help(
                "Quando recebeu?",
                "Data que o dinheiro caiu na conta",
                "date"
            )
            
            type_div = st.selectbox(
                "Tipo de dividendo:",
                ["Dividendo", "JCP (Juros sobre Capital Próprio)", "Não sei"],
                help="Se não souber, deixe 'Dividendo'"
            )
        
        submitted = st.form_submit_button("💾 Registrar Dividendo", type="primary", use_container_width=True)
        
        if submitted:
            if ticker and amount and date:
                show_success_message(f"Dividendo de {ticker.upper()} registrado!")
                return {
                    'ticker': ticker.upper(),
                    'amount': amount,
                    'date': date,
                    'type': type_div
                }
            else:
                show_warning_message("Preencha todos os campos obrigatórios!")
    
    return None

def show_quick_calculator():
    """Calculadora rápida de investimentos"""
    st.markdown("### 🧮 Calculadora Rápida")
    
    calc_type = st.selectbox(
        "O que você quer calcular?",
        [
            "💰 Quanto vou gastar para comprar ações",
            "📈 Qual seria meu lucro/prejuízo",
            "💵 Quanto de dividendo vou receber"
        ]
    )
    
    if "gastar" in calc_type:
        col1, col2, col3 = st.columns(3)
        with col1:
            qty = st.number_input("Quantas ações?", min_value=1, value=100)
        with col2:
            price = st.number_input("Preço por ação (R$)", min_value=0.01, value=10.00)
        with col3:
            total = qty * price
            st.metric("Total a gastar", f"R$ {total:,.2f}")
    
    elif "lucro" in calc_type:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            qty = st.number_input("Quantas ações tem?", min_value=1, value=100)
        with col2:
            buy_price = st.number_input("Comprou por (R$)", min_value=0.01, value=10.00)
        with col3:
            current_price = st.number_input("Preço atual (R$)", min_value=0.01, value=12.00)
        with col4:
            profit = qty * (current_price - buy_price)
            color = "green" if profit >= 0 else "red"
            st.markdown(f"<h3 style='color: {color}'>{'Lucro' if profit >= 0 else 'Prejuízo'}: R$ {abs(profit):,.2f}</h3>", unsafe_allow_html=True)
    
    else:  # dividendo
        col1, col2, col3 = st.columns(3)
        with col1:
            qty = st.number_input("Quantas ações tem?", min_value=1, value=100)
        with col2:
            div_per_share = st.number_input("Dividendo por ação (R$)", min_value=0.01, value=0.50)
        with col3:
            total_div = qty * div_per_share
            st.metric("Total a receber", f"R$ {total_div:,.2f}")