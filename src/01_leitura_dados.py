import pandas as pd

# Lê o arquivo CSV
carros = pd.read_csv("/storage/emulated/0/AutoMarket_Analytics/dados_brutos/carros.csv")

# Mostra as primeiras linhas
print(carros.head())

# Informações da base
print("\nInformações:")
print(carros.info())

# Estatísticas
print("\nEstatísticas:")
print(carros.describe())