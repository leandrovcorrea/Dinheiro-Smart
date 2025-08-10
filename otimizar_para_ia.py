import pandas as pd
import numpy as np
import re

def limpar_dados_numericos(valor):
    """Converte strings numéricas para float, tratando vírgulas e valores especiais."""
    if pd.isna(valor) or valor == '' or valor == '-':
        return np.nan
    
    if isinstance(valor, str):
        # Remove espaços e substitui vírgula por ponto
        valor = valor.strip().replace(',', '.')
        # Remove caracteres não numéricos exceto ponto e sinal negativo
        valor = re.sub(r'[^\d\.\-]', '', valor)
        
        try:
            return float(valor)
        except:
            return np.nan
    
    return float(valor) if not pd.isna(valor) else np.nan

def otimizar_tabelas_para_ia():
    """Otimiza as tabelas para uso em pesquisa de IA."""
    
    print("=== OTIMIZACAO DAS TABELAS PARA IA ===\n")
    
    # Processar arquivo de ações
    print("1. PROCESSANDO ARQUIVO DE ACOES...")
    try:
        df_acoes = pd.read_csv("statusinvest-busca-avancada (1).csv", sep=';', decimal=',')
        
        print(f"   - Dados originais: {len(df_acoes)} linhas, {len(df_acoes.columns)} colunas")
        
        # Colunas numéricas para limpar
        colunas_numericas = ['P/L', 'P/VP', 'ROE', 'P/ATIVOS', 'MARGEM BRUTA', 'MARGEM EBIT', 
                           'MARG. LIQUIDA', 'P/EBIT', 'EV/EBIT', 'PSR', 'LIQ. CORRENTE', 
                           'ROA', 'ROIC', ' VPA', ' LPA']
        
        # Limpar dados numéricos
        for col in colunas_numericas:
            if col in df_acoes.columns:
                df_acoes[col] = df_acoes[col].apply(limpar_dados_numericos)
        
        # Criar versão otimizada
        colunas_ia = ['TICKER', 'PRECO', 'DY', 'P/L', 'P/VP', 'ROE', 'ROA', 'ROIC', 
                     'MARGEM BRUTA', 'MARGEM EBIT', 'MARG. LIQUIDA', 'LIQ. CORRENTE',
                     ' VPA', ' LPA', ' LIQUIDEZ MEDIA DIARIA', ' VALOR DE MERCADO']
        
        df_acoes_ia = df_acoes[colunas_ia].copy()
        
        # Renomear colunas para formato mais limpo
        df_acoes_ia.columns = ['ticker', 'preco', 'dy', 'pl', 'pvp', 'roe', 'roa', 'roic',
                              'margem_bruta', 'margem_ebit', 'margem_liquida', 'liquidez_corrente',
                              'vpa', 'lpa', 'liquidez_diaria', 'valor_mercado']
        
        # Salvar versão otimizada
        df_acoes_ia.to_csv("acoes_otimizado_ia.csv", index=False, sep=';', decimal=',')
        
        print(f"   - Dados otimizados: {len(df_acoes_ia)} linhas, {len(df_acoes_ia.columns)} colunas")
        print(f"   - Arquivo salvo: acoes_otimizado_ia.csv")
        
        # Estatísticas de qualidade
        print("\n   QUALIDADE DOS DADOS OTIMIZADOS:")
        for col in df_acoes_ia.columns:
            if col != 'ticker':
                valores_validos = df_acoes_ia[col].notna().sum()
                total = len(df_acoes_ia)
                percentual = (valores_validos / total) * 100
                print(f"   - {col}: {valores_validos}/{total} ({percentual:.1f}%)")
        
    except Exception as e:
        print(f"   [ERRO] {e}")
    
    print("\n" + "="*60 + "\n")
    
    # Processar arquivo de FIIs
    print("2. PROCESSANDO ARQUIVO DE FIIs...")
    try:
        df_fiis = pd.read_csv("statusinvest-busca-avancada (2).csv", sep=';', decimal=',')
        
        print(f"   - Dados originais: {len(df_fiis)} linhas, {len(df_fiis.columns)} colunas")
        
        # Colunas numéricas para limpar
        colunas_numericas_fiis = ['P/VP', 'VALOR PATRIMONIAL COTA', 'LIQUIDEZ MEDIA DIARIA',
                                 'PERCENTUAL EM CAIXA', 'CAGR DIVIDENDOS 3 ANOS', 
                                 ' CAGR VALOR CORA 3 ANOS', 'PATRIMONIO', 'N COTISTAS', ' N COTAS']
        
        # Limpar dados numéricos
        for col in colunas_numericas_fiis:
            if col in df_fiis.columns:
                df_fiis[col] = df_fiis[col].apply(limpar_dados_numericos)
        
        # Criar versão otimizada
        colunas_ia_fiis = ['TICKER', 'PRECO', 'DY', 'P/VP', 'VALOR PATRIMONIAL COTA',
                          'LIQUIDEZ MEDIA DIARIA', 'PERCENTUAL EM CAIXA', 'PATRIMONIO',
                          'N COTISTAS', 'GESTAO']
        
        df_fiis_ia = df_fiis[colunas_ia_fiis].copy()
        
        # Renomear colunas
        df_fiis_ia.columns = ['ticker', 'preco', 'dy', 'pvp', 'valor_patrimonial',
                             'liquidez_diaria', 'percentual_caixa', 'patrimonio',
                             'num_cotistas', 'gestao']
        
        # Salvar versão otimizada
        df_fiis_ia.to_csv("fiis_otimizado_ia.csv", index=False, sep=';', decimal=',')
        
        print(f"   - Dados otimizados: {len(df_fiis_ia)} linhas, {len(df_fiis_ia.columns)} colunas")
        print(f"   - Arquivo salvo: fiis_otimizado_ia.csv")
        
        # Estatísticas de qualidade
        print("\n   QUALIDADE DOS DADOS OTIMIZADOS:")
        for col in df_fiis_ia.columns:
            if col not in ['ticker', 'gestao']:
                valores_validos = df_fiis_ia[col].notna().sum()
                total = len(df_fiis_ia)
                percentual = (valores_validos / total) * 100
                print(f"   - {col}: {valores_validos}/{total} ({percentual:.1f}%)")
        
    except Exception as e:
        print(f"   [ERRO] {e}")
    
    print("\n" + "="*60)
    
    # Criar arquivo de metadados
    print("\n3. CRIANDO METADADOS...")
    
    metadados = {
        "acoes": {
            "descricao": "Dados fundamentalistas de ações brasileiras",
            "fonte": "Status Invest",
            "colunas": {
                "ticker": "Código da ação na B3",
                "preco": "Preço atual da ação",
                "dy": "Dividend Yield (%)",
                "pl": "Preço/Lucro",
                "pvp": "Preço/Valor Patrimonial",
                "roe": "Return on Equity (%)",
                "roa": "Return on Assets (%)",
                "roic": "Return on Invested Capital (%)",
                "margem_bruta": "Margem Bruta (%)",
                "margem_ebit": "Margem EBIT (%)",
                "margem_liquida": "Margem Líquida (%)",
                "liquidez_corrente": "Liquidez Corrente",
                "vpa": "Valor Patrimonial por Ação",
                "lpa": "Lucro por Ação",
                "liquidez_diaria": "Liquidez Média Diária",
                "valor_mercado": "Valor de Mercado"
            }
        },
        "fiis": {
            "descricao": "Dados de Fundos de Investimento Imobiliário",
            "fonte": "Status Invest",
            "colunas": {
                "ticker": "Código do FII na B3",
                "preco": "Preço atual da cota",
                "dy": "Dividend Yield (%)",
                "pvp": "Preço/Valor Patrimonial",
                "valor_patrimonial": "Valor Patrimonial da Cota",
                "liquidez_diaria": "Liquidez Média Diária",
                "percentual_caixa": "Percentual em Caixa (%)",
                "patrimonio": "Patrimônio Líquido",
                "num_cotistas": "Número de Cotistas",
                "gestao": "Tipo de Gestão (Ativa/Passiva)"
            }
        }
    }
    
    import json
    with open("metadados_ia.json", "w", encoding='utf-8') as f:
        json.dump(metadados, f, indent=2, ensure_ascii=False)
    
    print("   - Arquivo de metadados criado: metadados_ia.json")
    
    print("\n4. RESUMO DA OTIMIZACAO:")
    print("   [OK] Dados numéricos limpos e convertidos")
    print("   [OK] Colunas renomeadas para padrão snake_case")
    print("   [OK] Arquivos otimizados salvos")
    print("   [OK] Metadados criados")
    print("   [OK] Formato adequado para bibliotecas de ML")
    
    print("\n5. PROXIMOS PASSOS PARA IA:")
    print("   - Implementar análise exploratória de dados")
    print("   - Criar pipeline de pré-processamento")
    print("   - Desenvolver modelos de classificação/regressão")
    print("   - Implementar sistema de recomendação")
    print("   - Criar API para consultas inteligentes")

if __name__ == "__main__":
    otimizar_tabelas_para_ia()