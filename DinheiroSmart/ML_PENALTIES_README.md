# Sistema de Penalidades Baseado em Machine Learning

## Visão Geral

O sistema de penalidades baseado em ML foi implementado para melhorar a análise de performance das ações na ferramenta Dinheiro $mart. Este sistema usa algoritmos de machine learning para prever a probabilidade de performance futura das ações e aplicar penalidades proporcionais ao risco identificado.

## Como Funciona

### 1. Modelo de Machine Learning

- **Algoritmo**: Random Forest Regressor
- **Features utilizadas**:
  - RSI (Relative Strength Index)
  - Razão SMA20/Preço Atual
  - Razão SMA50/Preço Atual
  - Volatilidade normalizada
  - Volume relativo
  - Retorno de 5 dias
  - Retorno de 20 dias

### 2. Treinamento do Modelo

O modelo é treinado automaticamente usando dados históricos de ações brasileiras populares:
- PETR4.SA, VALE3.SA, ITUB4.SA, BBDC4.SA, ABEV3.SA

O treinamento usa dados dos últimos 2 anos para criar um modelo preditivo robusto.

### 3. Predição de Performance

Para cada ação, o modelo:
1. Calcula indicadores técnicos dos últimos 3 meses
2. Faz uma predição do retorno futuro de 5 dias
3. Converte a predição em probabilidade usando função sigmoid
4. Retorna uma probabilidade entre 10% e 90%

### 4. Cálculo de Penalidades

A penalidade é calculada de forma inversamente proporcional à probabilidade:
- **Alta probabilidade (>60%)** → Penalidade baixa (< 20%)
- **Probabilidade moderada (40-60%)** → Penalidade média (20-30%)
- **Baixa probabilidade (<40%)** → Penalidade alta (> 30%)

## Integração na Ferramenta

### 1. Redistribuição por IA

Quando o usuário clica em "🧠 Redistribuição por IA":
1. O modelo ML é treinado (se necessário)
2. Para cada ação na carteira, calcula-se a penalidade ML
3. O score da ação é ajustado: `score_ajustado = score_original × (1 - penalidade)`
4. A distribuição final considera tanto análise fundamentalista quanto ML

### 2. Análise de Performance por ML

Nova seção na interface permite visualizar:
- Probabilidade de performance positiva para cada ação
- Penalidade aplicada
- Código de cores para fácil interpretação

## Benefícios

1. **Análise mais robusta**: Combina análise fundamentalista com análise técnica preditiva
2. **Redução de risco**: Identifica ações com maior probabilidade de performance negativa
3. **Decisões mais informadas**: Fornece dados quantitativos para tomada de decisão
4. **Adaptação automática**: O modelo se adapta às condições de mercado através do retreinamento

## Limitações

1. **Dados históricos**: Baseado em performance passada, não garante resultados futuros
2. **Mercado brasileiro**: Treinado especificamente para ações brasileiras
3. **Período de predição**: Focado em performance de curto prazo (5 dias)
4. **Dependência de dados**: Requer dados técnicos suficientes para funcionar

## Uso Recomendado

- Use como ferramenta complementar à análise fundamentalista
- Considere as penalidades como indicadores de risco, não verdades absolutas
- Reavalie periodicamente as recomendações conforme o mercado evolui
- Combine com sua própria pesquisa e análise antes de tomar decisões de investimento

## Aviso Legal

Este sistema é para fins educacionais e informativos. Não constitui recomendação de investimento. Sempre faça sua própria pesquisa antes de investir.