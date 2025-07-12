import streamlit as st

def show_welcome_card():
    """Exibe um card de boas-vindas amigável"""
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;">
            <h2 style="margin: 0 0 1rem 0; text-align: center;">🎯 Bem-vindo à sua jornada de investimentos!</h2>
            <p style="text-align: center; font-size: 1.1rem; margin: 0 0 1rem 0;">
                Aqui você pode analisar ações, gerenciar sua carteira e testar estratégias de forma simples e intuitiva.
            </p>
            <p style="text-align: center; font-size: 1rem; margin: 0; opacity: 0.9;">
                👆 Use as abas acima para navegar entre as diferentes funcionalidades
            </p>
        </div>
    """, unsafe_allow_html=True)

def show_quick_actions():
    """Exibe ações rápidas para usuários iniciantes"""
    st.markdown("### 🚀 Ações Rápidas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Analisar uma Ação", use_container_width=True, type="primary", key="btn_analyze"):
            st.info("👆 Clique na aba 'Analisar Ações' acima para começar!")
    
    with col2:
        if st.button("💼 Ver Minha Carteira", use_container_width=True, key="btn_portfolio"):
            st.info("👆 Clique na aba 'Meus Investimentos' acima para ver sua carteira!")
    
    with col3:
        if st.button("❓ Preciso de Ajuda", use_container_width=True, key="btn_help"):
            st.info("👆 Clique na aba 'Ajuda e Tutorial' acima para obter ajuda!")

def show_feature_cards():
    """Exibe cards explicativos das funcionalidades"""
    st.markdown("### 💡 O que você pode fazer aqui")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style="background: #f0f9ff; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #0ea5e9;">
                <h4 style="color: #0c4a6e; margin-top: 0;">📈 Para Iniciantes</h4>
                <ul style="color: #075985;">
                    <li>Analise ações sem conhecimento técnico</li>
                    <li>Veja se uma ação está cara ou barata</li>
                    <li>Acompanhe suas ações favoritas</li>
                    <li>Registre seus investimentos</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: #f0fdf4; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #22c55e;">
                <h4 style="color: #14532d; margin-top: 0;">🎯 Para Experientes</h4>
                <ul style="color: #166534;">
                    <li>Teste estratégias de investimento</li>
                    <li>Análise fundamentalista completa</li>
                    <li>Backtesting de estratégias</li>
                    <li>Comparação com benchmarks</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

def show_help_tooltip(text, tooltip):
    """Exibe um ícone de ajuda com tooltip"""
    st.markdown(f"""
        <span title="{tooltip}" style="cursor: help; color: #6b7280;">
            {text} ℹ️
        </span>
    """, unsafe_allow_html=True)

def show_success_message(message):
    """Exibe mensagem de sucesso amigável"""
    st.success(f"✅ {message}")

def show_warning_message(message):
    """Exibe mensagem de aviso amigável"""
    st.warning(f"⚠️ {message}")

def show_info_message(message):
    """Exibe mensagem informativa amigável"""
    st.info(f"💡 {message}")

def create_metric_card(title, value, delta=None, help_text=None):
    """Cria um card de métrica amigável"""
    if delta:
        st.metric(
            label=title,
            value=value,
            delta=delta,
            help=help_text
        )
    else:
        st.metric(
            label=title,
            value=value,
            help=help_text
        )

def show_loading_message(message="Carregando dados..."):
    """Exibe mensagem de carregamento amigável"""
    with st.spinner(f"🔄 {message}"):
        return True

def create_input_with_help(label, help_text, input_type="text", **kwargs):
    """Cria um input com texto de ajuda"""
    st.markdown(f"**{label}**")
    if help_text:
        st.markdown(f"<small style='color: #6b7280;'>{help_text}</small>", unsafe_allow_html=True)
    
    if input_type == "text":
        return st.text_input("", **kwargs)
    elif input_type == "number":
        return st.number_input("", **kwargs)
    elif input_type == "selectbox":
        return st.selectbox("", **kwargs)
    elif input_type == "date":
        return st.date_input("", **kwargs)

def show_tutorial_step(step_number, title, description, image_path=None):
    """Exibe um passo do tutorial"""
    st.markdown(f"""
        <div style="background: #fefce8; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #eab308;">
            <h4 style="color: #a16207; margin-top: 0;">Passo {step_number}: {title}</h4>
            <p style="color: #a16207; margin-bottom: 0;">{description}</p>
        </div>
    """, unsafe_allow_html=True)