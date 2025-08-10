#!/bin/bash

# Instalar dependências
pip install -r requirements.txt

# Criar diretório para Streamlit
mkdir -p ~/.streamlit

# Configurar Streamlit para servidor
echo '[server]\nheadless = true\nenableCORS = false\nport = $PORT' > ~/.streamlit/config.toml

# Garantir permissões de arquivos
chmod -R 777 .

# Criar diretórios para dados se não existirem
mkdir -p data
touch data/.keep

echo "Setup concluído com sucesso!"