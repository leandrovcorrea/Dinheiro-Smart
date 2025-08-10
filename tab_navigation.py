import streamlit as st

def handle_tab_navigation():
    """Gerencia navegação entre abas via botões"""
    
    # Mapeia ações para índices de abas
    tab_mapping = {
        "analyze": 4,    # Analisar Ações
        "portfolio": 1,  # Meus Investimentos  
        "help": 7        # Ajuda e Tutorial
    }
    
    # Verifica se há redirecionamento pendente
    if 'redirect_to_tab' in st.session_state:
        target_tab = st.session_state.redirect_to_tab
        
        if target_tab in tab_mapping:
            # Define a aba ativa
            st.session_state.active_tab_index = tab_mapping[target_tab]
            
            # Limpa o redirecionamento
            del st.session_state.redirect_to_tab
            
            # Força atualização da página
            st.rerun()

def create_navigation_buttons():
    """Cria botões de navegação rápida"""
    st.markdown("### 🚀 Navegação Rápida")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Ir para Análise", use_container_width=True, type="primary"):
            st.session_state.redirect_to_tab = "analyze"
            st.rerun()
    
    with col2:
        if st.button("💼 Ir para Carteira", use_container_width=True):
            st.session_state.redirect_to_tab = "portfolio"
            st.rerun()
    
    with col3:
        if st.button("❓ Ir para Ajuda", use_container_width=True):
            st.session_state.redirect_to_tab = "help"
            st.rerun()

def show_current_tab_info():
    """Mostra informações da aba atual"""
    if 'active_tab_index' in st.session_state:
        tab_names = [
            "Painel Principal", "Meus Investimentos", "Meus Dividendos", 
            "Lista de Acompanhamento", "Analisar Ações", "Análise do Mercado", 
            "Testar Estratégias", "Ajuda e Tutorial"
        ]
        
        current_tab = tab_names[st.session_state.active_tab_index]
        st.info(f"📍 Você está na aba: **{current_tab}**")