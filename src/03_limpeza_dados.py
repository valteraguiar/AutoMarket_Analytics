import pandas as pd

# Lê a base
carros = pd.read_csv("/storage/emulated/0/AutoMarket_Analytics/dados_brutos/carros.csv")

print("Quantidade inicial:", len(carros))

# Remove registros duplicados
carros = carros.drop_duplicates()

print("Após remover duplicados:", len(carros))

# Padroniza textos
carros["brand"] = carros["brand"].str.upper().str.strip()
carros["model"] = carros["model"].str.upper().str.strip()
carros["fuel"] = carros["fuel"].str.upper().str.strip()
carros["gear"] = carros["gear"].str.upper().str.strip()

# Cria coluna com idade do veículo
carros["idade_veiculo"] = carros["year_of_reference"] - carros["year_model"]

# Remove veículos com idade negativa (dados inconsistentes)
carros = carros[carros["idade_veiculo"] >= 0]

# Remove preços iguais ou menores que zero
carros = carros[carros["avg_price_brl"] > 0]

# Arredonda valores
carros["engine_size"] = carros["engine_size"].round(1)
carros["avg_price_brl"] = carros["avg_price_brl"].round(2)

print("\nResumo da base tratada:")
print(carros.info())

# Salva nova base
carros.to_csv(
    "/storage/emulated/0/AutoMarket_Analytics/dados_tratados/carros_tratados.csv",
    index=False
)

print("\nArquivo salvo com sucesso!")