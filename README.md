# Dinheiro $mart - Ferramenta de Análise e Gestão de Carteira

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Dinheiro $mart** é uma aplicação web desenvolvida em Python com Streamlit, projetada para auxiliar investidores na análise fundamentalista de ativos, gerenciamento de portfólio e teste de estratégias de investimento.

---

## 🚀 Funcionalidades Principais

A ferramenta é organizada em abas para uma navegação intuitiva:

### 🏠 Dashboard
- **Resumo da Carteira:** Métricas consolidadas como Custo Total, Valor Atual, Lucro/Prejuízo Realizado e Não Realizado, e Dividendos Recebidos.
- **Evolução do Patrimônio:** Gráfico interativo que mostra a rentabilidade da sua carteira ao longo do tempo.
- **Comparativo com Benchmarks:** Compare a performance da sua carteira com índices como IBOV, S&P 500, SMLL e IVVB11.
- **Distribuição de Ativos:** Gráficos de pizza para visualizar a alocação atual e a alocação ideal definida por você.

### 💼 Minha Carteira
- **Gestão de Transações:** Adicione, edite e remova transações de compra e venda de ativos.
- **Posição Consolidada:** Veja a quantidade, preço médio, cotação atual e o resultado de cada ativo em sua carteira.
- **Alocação Ideal:** Defina percentuais alvo para cada ativo e visualize o valor de ajuste necessário para o rebalanceamento.
- **Alertas de Preço:** Configure um preço-alvo para cada ativo e receba um alerta por e-mail quando ele for atingido.

### 👁️ Watchlist
- **Monitoramento de Ativos:** Adicione tickers de interesse para acompanhar suas cotações de forma rápida.
- **Notícias Recentes:** Acesse as últimas notícias (via Google News) para os ativos da sua watchlist.
- **Análise Rápida:** Inicie uma análise completa de qualquer ativo da watchlist com um único clique.

### 📊 Análise de Ativos
- **Modelos de Valuation:**
  - **Preço Justo de Graham:** Para ações, com base no LPA e perspectivas de crescimento.
  - **Número de Graham:** Valor intrínseco com base no LPA e VPA.
  - **Preço-Teto de Bazin:** Focado em dividendos.
  - **Preço-Teto para FIIs:** Com base no Dividend Yield desejado.
- **Indicadores Fundamentais:** P/L, P/VP, Dividend Yield, ROE, Dívida/Patrimônio e EV/EBITDA.
- **Análise Técnica (TradingView):** Obtenha a recomendação resumida (Compra Forte, Venda, Neutro, etc.) com base em indicadores técnicos diários.
- **Gráficos Interativos:** Visualize o histórico de preços e o histórico de dividendos pagos.

### 🧪 Backtesting
- **Teste de Estratégias:** Avalie o desempenho de estratégias de investimento com dados históricos.
- **Estratégia de Cruzamento de Médias Móveis:** Configure os períodos das médias curta e longa e veja o resultado financeiro, o número de trades e os sinais de compra/venda no gráfico.

### 👤 Autenticação de Usuários
- Sistema seguro de login, criação de conta e recuperação de senha por e-mail.

---

## 🛠️ Tecnologias Utilizadas

- **Backend & Frontend:** [Streamlit](https://streamlit.io/)
- **Análise de Dados:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Dados Financeiros:** [yfinance](https://pypi.org/project/yfinance/)
- **Visualização de Dados:** [Plotly Express](https://plotly.com/python/plotly-express/)
- **Análise Técnica:** [tradingview-ta](https://pypi.org/project/tradingview-ta/)
- **Notícias:** [feedparser](https://pypi.org/project/feedparser/)
- **Segurança:** [bcrypt](https://pypi.org/project/bcrypt/) para hashing de senhas.
- **Requisições HTTP:** [requests](https://pypi.org/project/requests/) (para API do Banco Central)

---

## ⚙️ Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

**1. Pré-requisitos:**
- Python 3.9 ou superior.
- `git` instalado.

**2. Clone o Repositório:**
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>
```

**3. Crie e Ative um Ambiente Virtual (Recomendado):**
```bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**4. Instale as Dependências:**
Crie um arquivo `requirements.txt` com o seguinte conteúdo:
```txt
streamlit
pandas
yfinance
tradingview-ta
requests
plotly
numpy
feedparser
bcrypt
```
Em seguida, instale os pacotes:
```bash
pip install -r requirements.txt
```

**5. Configure as Credenciais de E-mail (Opcional):**
Para que o envio de e-mails (recuperação de senha e alertas) funcione, crie um arquivo de segredos do Streamlit:

Crie a pasta e o arquivo: `.streamlit/secrets.toml`

Adicione o seguinte conteúdo, substituindo com suas credenciais (recomenda-se usar uma Senha de App do Gmail):
```toml
[email_credentials]
sender_email = "seu_email@gmail.com"
sender_password = "sua_senha_de_app_do_gmail"
```

**6. Execute a Aplicação:**
```bash
streamlit run app.py
```

---

## ⚠️ Avisos Importantes

- **Finalidade Educacional:** Esta é uma ferramenta para fins educacionais e de demonstração. **Não constitui recomendação de investimento.** As informações financeiras são obtidas de APIs de terceiros (como yfinance) e podem conter imprecisões ou atrasos. Faça sua própria pesquisa antes de tomar qualquer decisão de investimento.
- **Armazenamento de Dados:** O sistema de usuários, carteira e watchlist utiliza arquivos CSV para armazenamento. Embora as senhas sejam hasheadas com `bcrypt`, este método não é ideal para ambientes de produção. Para uma aplicação real, o uso de um banco de dados dedicado (como PostgreSQL, SQLite, etc.) é fortemente recomendado.

---

## ✒️ Autor

- **Leandro Correa** - GitHub
