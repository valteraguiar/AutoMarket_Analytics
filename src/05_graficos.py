import pandas as pd
import matplotlib.pyplot as plt

# Carrega a base tratada
carros = pd.read_csv("/storage/emulated/0/AutoMarket_Analytics/dados_tratados/carros_tratados.csv")

# Tamanho padrão das figuras
plt.rcParams["figure.figsize"] = (10,6)

# Gráfico 1 - Top 10 marcas por preço médio
#top_marcas = (
#    carros.groupby("brand")["avg_price_brl"]
#    .mean()
#    .sort_values(ascending=False)
#    .head(10)
#)

#plt.figure()

#top_marcas.plot(kind="bar")

#plt.title("Top 10 Marcas por Preço Médio")

#plt.xlabel("Marca")

#plt.ylabel("Preço Médio (R$)")

#plt.xticks(rotation=45)

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/top10_marcas_preco.png", dpi=300)
#plt.show()

# Gráfico 2 - Top 10 marcas mais presentes
#marcas = carros["brand"].value_counts().head(10)

#plt.figure();

#marcas.plot(kind="bar")

#plt.title("Marcas Mais Presentes")

#plt.xlabel("Marca")

#plt.ylabel("Quantidade")

#plt.xticks(rotation=45)

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/top10_maispresentes.png", dpi=300)
#plt.show()

# Gráfico 3 - Distribuição dos combustíveis
#combustivel = carros["fuel"].value_counts()

#plt.figure()

#combustivel.plot(kind="pie", autopct="%1.1f%%")

#plt.ylabel("")

#plt.title("Distribuição dos Combustíveis")

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/distrib_comb.png", dpi=300)
#plt.show()

# Gráfico 4 - Distribuição dos câmbios
#gear = carros["gear"].value_counts()

#plt.figure()

#gear.plot(kind="bar")

#plt.title("Distribuição dos Câmbios")

#plt.xlabel("Câmbio")

#plt.ylabel("Quantidade")

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/distrib_camb.png", dpi=300)
#plt.show()

# Gráfico 5 - Evolução do preço médio
#ano = (
#    carros.groupby("year_model")["avg_price_brl"]
#    .mean()
#)

#plt.figure()

#ano.plot()

#plt.title("Preço Médio por Ano do Modelo")

#plt.xlabel("Ano")

#plt.ylabel("Preço Médio")

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/evolucao_preco_medio.png", dpi=300)
#plt.show()

# Gráfico 6 - Preço por motorização
#motor = (
#    carros.groupby("engine_size")["avg_price_brl"]
#    .mean()
#)

#plt.figure()

#motor.plot(kind="bar")

#plt.title("Preço Médio por Motorização")

#plt.xlabel("Motor")

#plt.ylabel("Preço Médio")

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/preco_por_motorizacao.png", dpi=300)
#plt.show()

# Gráfico 7 - Boxplot (um dos mais usados)
#plt.figure()

#carros.boxplot(column="avg_price_brl")

#plt.title("Distribuição dos Preços")

#plt.tight_layout()

#plt.show()

#plt.tight_layout()
#plt.savefig("AutoMarket_Analytics/imagens/boxplot.png", dpi=300)
#plt.show()

#Gráfico 8 - Histograma
plt.figure()

carros["avg_price_brl"].hist(bins=30)

plt.title("Distribuição dos Preços")

plt.xlabel("Preço")

plt.ylabel("Quantidade")

plt.tight_layout()

plt.show()

plt.tight_layout()
plt.savefig("/storage/emulated/0/AutoMarket_Analytics/imagens/histograma.png", dpi=300)
plt.show()