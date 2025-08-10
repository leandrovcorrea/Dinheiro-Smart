import streamlit as st
import os
import sys
import importlib
import pandas as pd

def check_module(module_name):
    """Verifica se um módulo está instalado e disponível"""
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

def check_file(file_path):
    """Verifica se um arquivo existe"""
    return os.path.exists(file_path)

def main():
    st.title("🔍 Verificador de Deployment")
    st.write("Esta ferramenta verifica se todos os componentes necessários estão disponíveis.")
    
    # Informações do ambiente
    st.header("📊 Informações do Ambiente")
    st.write(f"**Python:** {sys.version}")
    st.write(f"**Diretório atual:** {os.getcwd()}")
    st.write(f"**Arquivos no diretório:**")
    files = os.listdir(".")
    st.write(", ".join(files))
    
    # Verificar módulos principais
    st.header("📚 Módulos Python")
    modules = [
        "streamlit", "pandas", "numpy", "yfinance", "plotly", 
        "sklearn", "tradingview_ta", "requests", "feedparser", 
        "bcrypt", "dotenv"
    ]
    
    module_status = []
    for module in modules:
        status = check_module(module)
        module_status.append({"Módulo": module, "Instalado": "✅" if status else "❌"})
    
    st.table(pd.DataFrame(module_status))
    
    # Verificar arquivos importantes
    st.header("📁 Arquivos do Projeto")
    files_to_check = [
        "app.py", "ml_predictor.py", "ml_strategies.py", 
        "carteira_widget.py", "beginner_guide.py", "user_guide.py"
    ]
    
    file_status = []
    for file in files_to_check:
        status = check_file(file)
        file_status.append({"Arquivo": file, "Existe": "✅" if status else "❌"})
    
    st.table(pd.DataFrame(file_status))
    
    # Verificar variáveis de ambiente
    st.header("🔐 Variáveis de Ambiente")
    env_vars = ["SENDER_EMAIL", "SENDER_PASSWORD", "API_KEY"]
    
    env_status = []
    for var in env_vars:
        value = os.getenv(var)
        status = "✅" if value else "❌"
        masked_value = "***" if value else "Não definido"
        env_status.append({"Variável": var, "Configurada": status, "Valor": masked_value})
    
    st.table(pd.DataFrame(env_status))
    
    # Instruções para corrigir problemas
    st.header("🛠️ Soluções para Problemas Comuns")
    
    st.markdown("""
    ### Módulos faltando
    Se algum módulo estiver faltando, verifique se ele está listado no arquivo `requirements.txt` e execute:
    ```
    pip install -r requirements.txt
    ```
    
    ### Arquivos faltando
    Certifique-se de que todos os arquivos Python necessários foram enviados para o repositório.
    
    ### Variáveis de ambiente não configuradas
    Configure as variáveis de ambiente no painel do Render:
    1. Acesse o dashboard do seu serviço
    2. Clique na aba "Environment"
    3. Adicione as variáveis necessárias
    """)

if __name__ == "__main__":
    main()