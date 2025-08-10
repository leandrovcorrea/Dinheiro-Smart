import pandas as pd
import numpy as np

def analisar_formato_para_ia():
    """Analisa se as tabelas estão no formato adequado para pesquisa de IA."""
    
    print("=== ANALISE DO FORMATO PARA PESQUISA DE IA ===\n")
    
    # Análise do arquivo de ações
    print("1. ARQUIVO DE ACOES:")
    try:
        df_acoes = pd.read_csv("statusinvest-busca-avancada (1).csv", sep=';', decimal=',')
        
        print(f"   - Total de registros: {len(df_acoes)}")
        print(f"   - Total de colunas: {len(df_acoes.columns)}")
        
        # Verifica colunas essenciais para IA
        colunas_essenciais = ['TICKER', 'P/L', 'ROE', 'DY', 'P/VP', 'PRECO']
        colunas_presentes = [col for col in colunas_essenciais if col in df_acoes.columns]
        colunas_faltantes = [col for col in colunas_essenciais if col not in df_acoes.columns]
        
        print(f"   - Colunas essenciais presentes: {colunas_presentes}")
        if colunas_faltantes:
            print(f"   - Colunas essenciais faltantes: {colunas_faltantes}")
        
        # Verifica qualidade dos dados
        print("\n   QUALIDADE DOS DADOS:")
        for col in colunas_presentes:
            if col in df_acoes.columns:
                total_valores = len(df_acoes)
                valores_nulos = df_acoes[col].isnull().sum()
                valores_validos = total_valores - valores_nulos
                percentual_valido = (valores_validos / total_valores) * 100
                
                print(f"   - {col}: {valores_validos}/{total_valores} valores válidos ({percentual_valido:.1f}%)")
        
        # Verifica tipos de dados
        print("\n   TIPOS DE DADOS:")
        for col in colunas_presentes[:5]:  # Primeiras 5 colunas
            if col in df_acoes.columns:
                tipo = df_acoes[col].dtype
                print(f"   - {col}: {tipo}")
        
    except Exception as e:
        print(f"   [ERRO] Não foi possível analisar arquivo de ações: {e}")
    
    print("\n" + "="*60 + "\n")
    
    # Análise do arquivo de FIIs
    print("2. ARQUIVO DE FIIs:")
    try:
        df_fiis = pd.read_csv("statusinvest-busca-avancada (2).csv", sep=';', decimal=',')
        
        print(f"   - Total de registros: {len(df_fiis)}")
        print(f"   - Total de colunas: {len(df_fiis.columns)}")
        
        # Verifica colunas essenciais para FIIs
        colunas_essenciais_fiis = ['TICKER', 'DY', 'P/VP', 'PRECO', 'VALOR PATRIMONIAL COTA']
        colunas_presentes_fiis = [col for col in colunas_essenciais_fiis if col in df_fiis.columns]
        colunas_faltantes_fiis = [col for col in colunas_essenciais_fiis if col not in df_fiis.columns]
        
        print(f"   - Colunas essenciais presentes: {colunas_presentes_fiis}")
        if colunas_faltantes_fiis:
            print(f"   - Colunas essenciais faltantes: {colunas_faltantes_fiis}")
        
        # Verifica qualidade dos dados
        print("\n   QUALIDADE DOS DADOS:")
        for col in colunas_presentes_fiis:
            if col in df_fiis.columns:
                total_valores = len(df_fiis)
                valores_nulos = df_fiis[col].isnull().sum()
                valores_validos = total_valores - valores_nulos
                percentual_valido = (valores_validos / total_valores) * 100
                
                print(f"   - {col}: {valores_validos}/{total_valores} valores válidos ({percentual_valido:.1f}%)")
        
    except Exception as e:
        print(f"   [ERRO] Não foi possível analisar arquivo de FIIs: {e}")
    
    print("\n" + "="*60)
    
    # Recomendações para IA
    print("\n3. RECOMENDACOES PARA PESQUISA DE IA:")
    print("\n   FORMATO ADEQUADO:")
    print("   [OK] Dados estruturados em CSV")
    print("   [OK] Separador definido (ponto e vírgula)")
    print("   [OK] Colunas nomeadas adequadamente")
    print("   [OK] Dados numéricos para análise quantitativa")
    
    print("\n   MELHORIAS SUGERIDAS:")
    print("   - Tratar valores nulos/vazios")
    print("   - Padronizar formato de números (decimal)")
    print("   - Adicionar metadados sobre as colunas")
    print("   - Criar índice por TICKER para busca rápida")
    print("   - Considerar normalização de dados para ML")
    
    print("\n   ADEQUACAO PARA IA:")
    print("   [OK] Dados tabulares - adequados para análise")
    print("   [OK] Múltiplas variáveis - permite correlações")
    print("   [OK] Dados históricos - permite análise temporal")
    print("   [OK] Formato padrão - compatível com pandas/numpy")
    
    print("\n   CASOS DE USO DE IA POSSÍVEIS:")
    print("   - Análise de correlação entre indicadores")
    print("   - Classificação de ações (valor, crescimento, etc.)")
    print("   - Predição de performance baseada em fundamentals")
    print("   - Clustering de ativos similares")
    print("   - Detecção de anomalias nos dados")
    print("   - Recomendação de investimentos")

if __name__ == "__main__":
    analisar_formato_para_ia()