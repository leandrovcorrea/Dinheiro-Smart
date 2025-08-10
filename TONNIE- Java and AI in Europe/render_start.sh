#!/bin/bash

# Este script é usado pelo Render para iniciar o aplicativo
# Ele executa o setup.sh e depois inicia o Streamlit

echo "Iniciando processo de deployment..."

# Executar setup
echo "Executando setup.sh..."
sh setup.sh

# Verificar se há arquivos Python essenciais
echo "Verificando arquivos essenciais..."
if [ ! -f "app.py" ]; then
  echo "ERRO: app.py não encontrado!"
  exit 1
fi

# Listar arquivos no diretório atual
echo "Arquivos no diretório:"
ls -la

# Iniciar o aplicativo Streamlit
echo "Iniciando Streamlit..."
streamlit run app.py --server.port=$PORT --server.enableCORS=false