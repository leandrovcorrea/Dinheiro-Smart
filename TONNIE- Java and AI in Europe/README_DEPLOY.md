# Guia de Implantação no Render

Este guia explica como implantar o aplicativo Dinheiro $mart no Render.

## Método 1: Implantação Automática (Recomendado)

### 1. Crie uma conta no Render

Acesse [render.com](https://render.com/) e crie uma conta gratuita.

### 2. Conecte seu repositório GitHub

1. No dashboard do Render, clique em "New" e selecione "Blueprint"
2. Conecte sua conta GitHub e selecione o repositório do projeto
3. O Render detectará automaticamente o arquivo `render.yaml` e configurará o serviço

### 3. Implante o serviço

Clique em "Apply" e aguarde a implantação.

## Método 2: Implantação Manual

### 1. Crie uma conta no Render

Acesse [render.com](https://render.com/) e crie uma conta gratuita.

### 2. Crie um novo Web Service

1. No dashboard do Render, clique em "New" e selecione "Web Service"
2. Conecte sua conta GitHub e selecione o repositório do projeto

### 3. Configure o serviço

Preencha os seguintes campos:
- **Name**: dinheiro-smart (ou outro nome de sua escolha)
- **Environment**: Python
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run app.py`

### 4. Implante o serviço

Clique em "Create Web Service" e aguarde a implantação.

## Arquivos de Configuração

O projeto já contém os arquivos necessários para implantação:

- **requirements.txt**: Lista todas as dependências do projeto
- **render.yaml**: Configuração automática para o Render
- **.streamlit/config.toml**: Configurações do Streamlit para produção

## Observações Importantes

- O plano gratuito do Render tem limitações de recursos e tempo de execução
- O aplicativo será desligado após períodos de inatividade
- Dados armazenados localmente (CSVs) serão perdidos quando o serviço for reiniciado

Para persistência de dados, considere usar um banco de dados externo como PostgreSQL ou MongoDB.