import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

st.title("🔎 Teste de Scraping - AgendaDividendos")

ticker = "PINE4"
url = f"https://www.agendadividendos.com/app/empresa/{ticker.lower()}/"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    tabela = soup.find("table", {"class": "table table-striped table-sm"})

    if not tabela:
        st.error("❌ Tabela não encontrada.")
    else:
        linhas = tabela.find_all("tr")[1:]
        dividendos = []

        for linha in linhas:
            colunas = linha.find_all("td")
            if len(colunas) >= 4:
                dividendos.append({
                    "Tipo": colunas[0].get_text(strip=True),
                    "Data Ex": colunas[1].get_text(strip=True),
                    "Pagamento": colunas[2].get_text(strip=True),
                    "Valor": colunas[3].get_text(strip=True)
                })

        if dividendos:
            df = pd.DataFrame(dividendos)
            st.dataframe(df)
        else:
            st.warning("⚠️ Nenhum dividendo encontrado.")
except Exception as e:
    st.error(f"Erro: {e}")