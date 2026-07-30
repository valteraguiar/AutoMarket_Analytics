import pandas as pd

carros = pd.read_csv("/storage/emulated/0/AutoMarket_Analytics/dados_brutos/carros.csv")

print("Colunas da base:\n")
print(carros.columns)

print("\nQuantidade de linhas:")
print(len(carros))

print("\nTipos das colunas:")
print(carros.dtypes)

print("\nValores nulos:")
print(carros.isnull().sum())