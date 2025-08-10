# Configurando Variáveis de Ambiente no Render

Este guia explica como configurar variáveis de ambiente para seu aplicativo Dinheiro $mart no Render.

## O que são variáveis de ambiente?

Variáveis de ambiente são valores que podem ser acessados pelo seu aplicativo em tempo de execução, sem precisar codificá-los diretamente no código. Elas são ideais para:

- Credenciais (senhas, chaves de API)
- Configurações específicas do ambiente
- Segredos que não devem ser expostos no código

## Como configurar no Render

1. Acesse o dashboard do seu serviço no Render
2. Clique na aba "Environment"
3. Na seção "Environment Variables", adicione suas variáveis:

| Nome da Variável | Valor |
|------------------|-------|
| SENDER_EMAIL     | seu_email@gmail.com |
| SENDER_PASSWORD  | sua_senha_de_app |
| API_KEY          | sua_chave_api |

4. Clique em "Save Changes"

## Como acessar no código

Para acessar essas variáveis no seu código Python:

```python
import os

# Obter variáveis de ambiente
email = os.getenv("SENDER_EMAIL")
senha = os.getenv("SENDER_PASSWORD")
api_key = os.getenv("API_KEY")

# Usar as variáveis
if email and senha:
    # Fazer algo com as credenciais
    print(f"Usando email: {email}")
else:
    print("Credenciais não configuradas")
```

## Variáveis recomendadas para o Dinheiro $mart

Para o envio de e-mails e alertas:
- `SENDER_EMAIL`: E-mail que enviará as notificações
- `SENDER_PASSWORD`: Senha de app do Gmail (não use sua senha normal)

Para APIs externas:
- `API_KEY`: Chave de API para serviços financeiros (se necessário)

## Desenvolvimento local

Para desenvolvimento local, você pode:

1. Criar um arquivo `.env` na raiz do projeto
2. Adicionar suas variáveis no formato:
   ```
   SENDER_EMAIL=seu_email@gmail.com
   SENDER_PASSWORD=sua_senha_de_app
   API_KEY=sua_chave_api
   ```
3. Instalar a biblioteca python-dotenv:
   ```
   pip install python-dotenv
   ```
4. Carregar as variáveis no seu código:
   ```python
   from dotenv import load_dotenv
   load_dotenv()  # carrega variáveis do arquivo .env
   ```

**Importante**: Nunca comite o arquivo `.env` no Git. Adicione-o ao `.gitignore`.