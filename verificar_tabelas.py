import pandas as pd
import os

def verificar_formato_tabelas():
    """Verifica o formato das tabelas do Status Invest."""
    
    print("=== VERIFICACAO DAS TABELAS STATUS INVEST ===\n")
    
    # Verifica arquivo de ações
    arquivo_acoes = "statusinvest-busca-avancada (1).csv"
    if os.path.exists(arquivo_acoes):
        print(f"[OK] Arquivo encontrado: {arquivo_acoes}")
        try:
            df_acoes = pd.read_csv(arquivo_acoes, sep=';', decimal=',')
            print(f"Linhas: {len(df_acoes)}")
            print(f"Colunas: {list(df_acoes.columns)}")
            print(f"Exemplo de dados:")
            print(df_acoes.head(2))
            print()
        except Exception as e:
            print(f"[ERRO] Erro ao ler arquivo: {e}")
            # Tenta outros separadores
            try:
                df_acoes = pd.read_csv(arquivo_acoes, sep=',', decimal='.')
                print(f"[OK] Lido com separador ',' e decimal '.'")
                print(f"Colunas: {list(df_acoes.columns)}")
            except:
                print("[ERRO] Nao foi possivel ler com formatos alternativos")
    else:
        print(f"[ERRO] Arquivo nao encontrado: {arquivo_acoes}")
    
    print("\n" + "="*50 + "\n")
    
    # Verifica arquivo de FIIs
    arquivo_fiis = "statusinvest-busca-avancada (2).csv"
    if os.path.exists(arquivo_fiis):
        print(f"[OK] Arquivo encontrado: {arquivo_fiis}")
        try:
            df_fiis = pd.read_csv(arquivo_fiis, sep=';', decimal=',')
            print(f"Linhas: {len(df_fiis)}")
            print(f"Colunas: {list(df_fiis.columns)}")
            print(f"Exemplo de dados:")
            print(df_fiis.head(2))
            print()
        except Exception as e:
            print(f"[ERRO] Erro ao ler arquivo: {e}")
            # Tenta outros separadores
            try:
                df_fiis = pd.read_csv(arquivo_fiis, sep=',', decimal='.')
                print(f"[OK] Lido com separador ',' e decimal '.'")
                print(f"Colunas: {list(df_fiis.columns)}")
            except:
                print("[ERRO] Nao foi possivel ler com formatos alternativos")
    else:
        print(f"[ERRO] Arquivo nao encontrado: {arquivo_fiis}")
    
    print("\n" + "="*50)
    print("INSTRUCOES:")
    print("1. Coloque os arquivos CSV na pasta do projeto")
    print("2. Certifique-se que tem as colunas: TICKER, P/L, ROE, DY")
    print("3. Execute novamente para verificar")

if __name__ == "__main__":
    verificar_formato_tabelas()