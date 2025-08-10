from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

ticker = "PINE4"
url = f"https://www.agendadividendos.com/app/empresa/{ticker.lower()}/"

# Configura o Chrome em modo headless
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Inicia o navegador
driver = webdriver.Chrome(options=options)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get(url)

try:
    tabela = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-striped"))
    )
except:
    print("❌ A tabela não apareceu após 15 segundos.")
    driver.quit()
    exit()

try:
    linhas = tabela.find_elements(By.TAG_NAME, "tr")[1:]

    dividendos = []
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        if len(colunas) >= 4:
            dividendos.append({
                "Tipo": colunas[0].text.strip(),
                "Data Ex": colunas[1].text.strip(),
                "Pagamento": colunas[2].text.strip(),
                "Valor": colunas[3].text.strip()
            })

    df = pd.DataFrame(dividendos)
    print(df)

except Exception as e:
    print("❌ Erro ao extrair dados:", e)

driver.quit()