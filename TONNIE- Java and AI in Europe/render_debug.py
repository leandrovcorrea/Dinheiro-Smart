import streamlit as st
import os
import sys
import traceback

def main():
    st.title("🐞 Depurador para Render")
    st.write("Esta ferramenta ajuda a identificar problemas no deployment do Render.")
    
    # Informações básicas do ambiente
    st.header("Informações do Sistema")
    st.code(f"""
Python: {sys.version}
Diretório: {os.getcwd()}
Plataforma: {sys.platform}
Arquivos: {', '.join(os.listdir('.')[:10])}{'...' if len(os.listdir('.')) > 10 else ''}
    """)
    
    # Testar importações críticas
    st.header("Teste de Importações")
    
    with st.expander("Testar importações básicas", expanded=True):
        test_imports = [
            "streamlit", "pandas", "numpy", "yfinance", 
            "plotly", "sklearn", "tradingview_ta", "requests", 
            "feedparser", "bcrypt"
        ]
        
        for module in test_imports:
            try:
                st.write(f"Importando {module}...")
                exec(f"import {module}")
                st.success(f"✅ {module} importado com sucesso")
            except Exception as e:
                st.error(f"❌ Erro ao importar {module}: {str(e)}")
    
    # Testar importações de módulos locais
    with st.expander("Testar importações de módulos locais", expanded=True):
        local_modules = [
            "ml_predictor", "ml_strategies", "carteira_widget", 
            "beginner_guide", "user_guide"
        ]
        
        for module in local_modules:
            try:
                st.write(f"Importando {module}...")
                exec(f"import {module}")
                st.success(f"✅ {module} importado com sucesso")
            except Exception as e:
                st.error(f"❌ Erro ao importar {module}: {str(e)}")
                st.code(traceback.format_exc())
    
    # Testar acesso a arquivos
    st.header("Teste de Acesso a Arquivos")
    
    with st.expander("Verificar permissões de arquivos", expanded=True):
        try:
            # Tentar criar um arquivo temporário
            with open("temp_test.txt", "w") as f:
                f.write("Teste de escrita")
            
            st.success("✅ Escrita de arquivo bem-sucedida")
            
            # Tentar ler o arquivo
            with open("temp_test.txt", "r") as f:
                content = f.read()
            
            st.success(f"✅ Leitura de arquivo bem-sucedida: '{content}'")
            
            # Limpar
            os.remove("temp_test.txt")
            st.success("✅ Remoção de arquivo bem-sucedida")
        except Exception as e:
            st.error(f"❌ Erro de acesso a arquivos: {str(e)}")
            st.code(traceback.format_exc())
    
    # Testar variáveis de ambiente
    st.header("Teste de Variáveis de Ambiente")
    
    with st.expander("Verificar variáveis de ambiente", expanded=True):
        env_vars = ["SENDER_EMAIL", "SENDER_PASSWORD", "API_KEY", "PORT"]
        
        for var in env_vars:
            value = os.environ.get(var)
            if value:
                masked = "***" if "PASSWORD" in var or "KEY" in var else value
                st.success(f"✅ {var} = {masked}")
            else:
                st.warning(f"⚠️ {var} não está definida")
    
    # Instruções para correção
    st.header("Como corrigir problemas comuns")
    
    st.markdown("""
    ### 1. Módulos Python faltando
    
    Verifique se todos os módulos necessários estão no `requirements.txt`:
    ```
    streamlit
    pandas
    numpy
    yfinance
    plotly
    scikit-learn
    tradingview-ta
    requests
    feedparser
    bcrypt
    python-dotenv
    ```
    
    ### 2. Arquivos Python faltando
    
    Certifique-se de que todos os arquivos `.py` foram enviados para o repositório.
    
    ### 3. Problemas de permissão
    
    No Render, adicione estas linhas ao `setup.sh`:
    ```bash
    mkdir -p ~/.streamlit
    chmod -R 777 .
    ```
    
    ### 4. Variáveis de ambiente
    
    Configure as variáveis no painel do Render (Environment tab).
    """)

if __name__ == "__main__":
    main()