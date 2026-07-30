import pandas as pd

# Carrega a base tratada
carros = pd.read_csv("/storage/emulated/0/AutoMarket_Analytics/dados_tratados/carros_tratados.csv")

def mostrar_resultado(titulo, resultado):
    print("\n" + "="*70)
    print(titulo)
    print("="*70)
    print(resultado)
    print()

print("="*60)
print("RESUMO GERAL")
print("="*60)

print(f"Quantidade de registros: {len(carros)}")
print(f"Quantidade de marcas: {carros['brand'].nunique()}")
print(f"Quantidade de modelos: {carros['model'].nunique()}")

print("\nPreço médio: R$ {:.2f}".format(carros["avg_price_brl"].mean()))
print("Preço máximo: R$ {:.2f}".format(carros["avg_price_brl"].max()))
print("Preço mínimo: R$ {:.2f}".format(carros["avg_price_brl"].min()))

# Quais são as 10 marcas com maior preço médio?
top_marcas = (
    carros.groupby("brand")["avg_price_brl"]
    .mean().round(2)
    .sort_values(ascending=False)
)

mostrar_resultado("TOP 10 MARCAS POR PREÇO MÉDIO", top_marcas.head(10))

# Quais são as marcas mais presentes na base?
marcas = carros["brand"].value_counts()

mostrar_resultado("TOP 10 MARCAS MAIS PRESENTES", marcas.head(10))

# Qual é a distribuição dos combustíveis?
combustivel = carros["fuel"].value_counts()

mostrar_resultado("DISTRIBUIÇÃO DOS COMBUSTÍVEIS", combustivel)

# Qual é a distribuição dos câmbios?
cambio = carros["gear"].value_counts()

mostrar_resultado("DISTRIBUIÇÃO DOS CÂMBIOS", cambio)

# Quais modelos possuem maior preço médio?
modelos = (
    carros.groupby("model")["avg_price_brl"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

mostrar_resultado("PREÇO MÉDIO POR MODELO", modelos.head(20))

# Qual é o preço médio por ano do modelo?
ano = (
    carros.groupby("year_model")["avg_price_brl"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

mostrar_resultado("PREÇO MÉDIO POR ANO DE MODELO", ano)

# Qual é o preço médio por tipo de câmbio?
gear = (
    carros.groupby("gear")["avg_price_brl"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

mostrar_resultado("PREÇO MÉDIO POR TIPO DE CÂMBIO", gear)

# Qual é o preço médio por combustível?
fuel = (
    carros.groupby("fuel")["avg_price_brl"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

mostrar_resultado("PREÇO MÉDIO POR TIPO DE COMBUSTÍVEL", fuel)

# Qual é o preço médio por motorização?
motor = (
    carros.groupby("engine_size")["avg_price_brl"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

mostrar_resultado("PREÇO MÉDIO POR TIPO DE MOTORIZAÇÃO", motor)