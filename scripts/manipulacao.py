import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
file_path = 'caminhoDoArquivo/Meganium_Sales_data.xlsx'
df = pd.read_excel(file_path)

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Análise básica
print(df.describe())
print(df.info())

# Verificar valores nulos
print("Valores nulos por coluna:")
print(df.isnull().sum())

# Visualizar a distribuição de uma coluna específica (substitua 'nome_da_coluna' pelo nome real da coluna)
coluna = 'nome_da_coluna'  # Substitua pelo nome da coluna desejada
if coluna in df.columns:
    df[coluna].hist()
    plt.title(f'Distribuição da coluna {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()
else:
    print(f"A coluna '{coluna}' não existe no DataFrame.")

# Agrupar dados e calcular estatísticas (substitua 'outra_coluna' pelo nome real da coluna)
outra_coluna = 'outra_coluna'  # Substitua pelo nome da coluna desejada
if outra_coluna in df.columns:
    grouped_df = df.groupby(outra_coluna).mean()
    print(f"Estatísticas agrupadas por '{outra_coluna}':")
    print(grouped_df)
else:
    print(f"A coluna '{outra_coluna}' não existe no DataFrame.")