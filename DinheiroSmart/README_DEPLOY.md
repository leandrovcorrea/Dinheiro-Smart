# Como Publicar o Dinheiro Smart

## Opções de Deploy

### 1. Streamlit Cloud (Mais Fácil)
1. Faça push do código para GitHub
2. Vá em [share.streamlit.io](https://share.streamlit.io)
3. Conecte sua conta GitHub
4. Selecione o repositório
5. Arquivo principal: `app.py`
6. Deploy automático!

### 2. Heroku
1. Instale Heroku CLI
2. `heroku create nome-do-app`
3. `git push heroku main`
4. `heroku open`

### 3. Render
1. Conecte GitHub em [render.com](https://render.com)
2. Selecione "Web Service"
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### 4. Vercel
1. Conecte GitHub em [vercel.com](https://vercel.com)
2. Deploy automático com vercel.json

### 5. Railway
1. Conecte GitHub em [railway.app](https://railway.app)
2. Deploy automático

## Arquivos Criados
- `Procfile` - Heroku
- `runtime.txt` - Versão Python
- `requirements.txt` - Dependências
- `render.yaml` - Render
- `vercel.json` - Vercel
- `app.yaml` - Google App Engine
- `setup.sh` - Script Heroku
- `.streamlit/config.toml` - Configuração Streamlit

## Comandos Git
```bash
git add .
git commit -m "Deploy configuration"
git push origin main
```

## Recomendação
Use **Streamlit Cloud** - é gratuito e específico para apps Streamlit!