# Prompt para Análise de Dados com Pandas e Matplotlib

## Objetivo

Realizar uma análise básica de um conjunto de dados de vendas armazenado em um arquivo Excel. O script (manipulacao.py) carrega os dados, exibe informações básicas, verifica valores nulos, visualiza a distribuição de uma coluna específica e agrupa dados para calcular estatísticas.

## Passos

1. **Carregar o arquivo Excel**:
    - O caminho do arquivo é especificado pela variável `file_path`.
    - O arquivo é carregado em um DataFrame do Pandas.

2. **Exibir as primeiras linhas do DataFrame**:
    - Utiliza `df.head()` para mostrar as primeiras linhas do DataFrame.

3. **Análise básica**:
    - Utiliza `df.describe()` para exibir estatísticas descritivas.
    - Utiliza `df.info()` para exibir informações sobre o DataFrame.

4. **Verificar valores nulos**:
    - Utiliza `df.isnull().sum()` para contar valores nulos por coluna.

5. **Visualizar a distribuição de uma coluna específica**:
    - A coluna a ser visualizada é especificada pela variável `coluna`.
    - Utiliza `df[coluna].hist()` para criar um histograma da coluna.
    - Exibe o histograma utilizando Matplotlib.

6. **Agrupar dados e calcular estatísticas**:
    - A coluna para agrupamento é especificada pela variável `outra_coluna`.
    - Utiliza `df.groupby(outra_coluna).mean()` para calcular a média dos grupos.
    - Exibe as estatísticas agrupadas.
