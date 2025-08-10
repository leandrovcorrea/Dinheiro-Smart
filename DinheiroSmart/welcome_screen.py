import streamlit as st

def show_welcome_screen():
    """Tela de boas-vindas para novos usuários"""
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem; border-radius: 15px; margin-bottom: 2rem; text-align: center;'>
        <h1 style='color: white; font-size: 3rem; margin: 0;'>🎉 Bem-vindo ao Dinheiro $mart!</h1>
        <p style='color: white; font-size: 1.2rem; margin: 1rem 0;'>Sua ferramenta completa para análise de investimentos</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Vídeo tutorial ou GIF explicativo (placeholder)
    st.markdown("""
    <div style='text-align: center; margin: 2rem 0;'>
        <div style='background: #f0f2f6; padding: 3rem; border-radius: 10px; border: 2px dashed #ccc;'>
            <h3>🎬 Vídeo Tutorial (Em breve)</h3>
            <p>Aprenda a usar a ferramenta em 3 minutos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Cards com funcionalidades principais
    st.markdown("## 🚀 O que você pode fazer:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; margin-bottom: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📊</div>
            <h3 style='color: #333; margin-bottom: 1rem;'>Analisar Ações</h3>
            <p style='color: #666; font-size: 0.9rem;'>Descubra se uma ação está cara ou barata usando modelos matemáticos comprovados</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; margin-bottom: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>💼</div>
            <h3 style='color: #333; margin-bottom: 1rem;'>Gerenciar Carteira</h3>
            <p style='color: #666; font-size: 0.9rem;'>Acompanhe seus investimentos e veja sugestões de rebalanceamento automático</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; margin-bottom: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🤖</div>
            <h3 style='color: #333; margin-bottom: 1rem;'>IA Avançada</h3>
            <p style='color: #666; font-size: 0.9rem;'>Use inteligência artificial para otimizar sua carteira e reduzir riscos</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Passos simples para começar
    st.markdown("## 🎯 Como começar em 3 passos:")
    
    step1, step2, step3 = st.columns(3)
    
    with step1:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='background: #4CAF50; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;'>1</div>
            <h4>Adicione suas ações</h4>
            <p style='font-size: 0.9rem; color: #666;'>Vá em "Minha Carteira" e adicione as ações que você possui</p>
        </div>
        """, unsafe_allow_html=True)
    
    with step2:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='background: #2196F3; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;'>2</div>
            <h4>Analise uma ação</h4>
            <p style='font-size: 0.9rem; color: #666;'>Use "Análise de Ativos" para descobrir se uma ação está cara ou barata</p>
        </div>
        """, unsafe_allow_html=True)
    
    with step3:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <div style='background: #FF9800; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;'>3</div>
            <h4>Veja o Dashboard</h4>
            <p style='font-size: 0.9rem; color: #666;'>Acompanhe a evolução da sua carteira e compare com índices</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Botão de ação
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Começar Agora!", use_container_width=True, type="primary"):
            st.session_state.show_welcome = False
            st.rerun()
    
    # Testimonial ou exemplo
    st.markdown("---")
    st.markdown("""
    ### 💡 Exemplo Prático:
    
    **Situação:** João quer saber se deve comprar ações da Petrobras (PETR4)
    
    **Solução:** 
    1. Ele digita "PETR4" na aba "Análise de Ativos"
    2. A ferramenta mostra que o preço justo é R$ 35,00
    3. O preço atual está R$ 30,00
    4. **Resultado:** Margem de segurança de +16,7% - pode ser uma boa oportunidade!
    
    ✅ **Decisão informada em menos de 30 segundos!**
    """)

def show_quick_start_tips():
    """Dicas rápidas para começar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎯 Dicas Rápidas:")
    st.sidebar.info("""
    **Para começar:**
    1. Vá em "Minha Carteira"
    2. Adicione suas ações
    3. Veja o Dashboard
    
    **Precisa de ajuda?**
    Clique na aba "❓ Ajuda"
    """)

def check_first_time_user():
    """Verifica se é a primeira vez do usuário"""
    if 'show_welcome' not in st.session_state:
        st.session_state.show_welcome = True
    
    return st.session_state.show_welcome