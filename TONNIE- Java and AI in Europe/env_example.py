import os
import streamlit as st
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env (para desenvolvimento local)
load_dotenv()

def enviar_email_exemplo(destinatario, assunto, corpo):
    """Exemplo de função que usa variáveis de ambiente para enviar e-mail"""
    try:
        # Obter credenciais das variáveis de ambiente
        remetente = os.getenv("SENDER_EMAIL")
        senha = os.getenv("SENDER_PASSWORD")
        
        # Verificar se as credenciais estão disponíveis
        if not remetente or not senha:
            return False, "Credenciais não configuradas"
            
        # Código para enviar e-mail usando as credenciais
        # ...
        
        return True, None
    except Exception as e:
        return False, str(e)

# Exemplo de uso em uma página Streamlit
def mostrar_exemplo():
    st.title("Exemplo de Variáveis de Ambiente")
    
    # Verificar se as variáveis estão configuradas
    email = os.getenv("SENDER_EMAIL")
    senha = os.getenv("SENDER_PASSWORD")
    api_key = os.getenv("API_KEY")
    
    if email:
        st.success(f"E-mail configurado: {email}")
    else:
        st.error("E-mail não configurado")
        
    if senha:
        st.success("Senha configurada")
    else:
        st.error("Senha não configurada")
        
    if api_key:
        st.success("API Key configurada")
    else:
        st.error("API Key não configurada")
    
    # Botão para testar envio de e-mail
    if st.button("Testar Envio de E-mail"):
        destinatario = st.text_input("E-mail de destino")
        if destinatario:
            sucesso, erro = enviar_email_exemplo(destinatario, "Teste", "Teste de envio")
            if sucesso:
                st.success("E-mail enviado com sucesso!")
            else:
                st.error(f"Erro ao enviar e-mail: {erro}")

if __name__ == "__main__":
    mostrar_exemplo()