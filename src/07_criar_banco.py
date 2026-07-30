import sqlite3
import pandas as pd

# Caminhos
csv = "/storage/emulated/0/AutoMarket_Analytics/dados_tratados/carros_tratados.csv"
banco = "/storage/emulated/0/AutoMarket_Analytics/database.db"

# Lê os dados
carros = pd.read_csv(csv)

# Conecta ao banco
conexao = sqlite3.connect(banco)

# Cria a tabela
carros.to_sql(
    "carros",
    conexao,
    if_exists="replace",
    index=False
)

print("Banco criado com sucesso!")

conexao.close()