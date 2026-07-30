import sqlite3
import pandas as pd
import os

# ==================================
# CAMINHOS
# ==================================

CAMINHO_BANCO = "/storage/emulated/0/AutoMarket_Analytics/database.db"

PASTA_RELATORIOS = "/storage/emulated/0/AutoMarket_Analytics/relatorios"

ARQUIVO_EXCEL = os.path.join(
    PASTA_RELATORIOS,
    "Relatorio_Analises.xlsx"
)

# Cria a pasta caso ela não exista
os.makedirs(PASTA_RELATORIOS, exist_ok=True)

# ==================================
# CONSULTAS
# ==================================

consultas = {

"Resumo Geral":
"""
SELECT
COUNT(*) AS Total_Registros,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio,
MIN(avg_price_brl) AS Menor_Preco,
MAX(avg_price_brl) AS Maior_Preco
FROM carros;
""",

"Top Marcas":
"""
SELECT
brand,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio
FROM carros
GROUP BY brand
ORDER BY Preco_Medio DESC
LIMIT 20;
""",

"Quantidade por Marca":
"""
SELECT
brand,
COUNT(*) AS Quantidade
FROM carros
GROUP BY brand
ORDER BY Quantidade DESC;
""",

"Combustíveis":
"""
SELECT
fuel,
COUNT(*) AS Quantidade,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio
FROM carros
GROUP BY fuel
ORDER BY Preco_Medio DESC;
""",

"Câmbios":
"""
SELECT
gear,
COUNT(*) AS Quantidade,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio
FROM carros
GROUP BY gear
ORDER BY Preco_Medio DESC;
""",

"Motorização":
"""
SELECT
engine_size,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio
FROM carros
GROUP BY engine_size
ORDER BY engine_size;
""",

"Ano Modelo":
"""
SELECT
year_model,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio
FROM carros
GROUP BY year_model
ORDER BY year_model;
""",

"Top Modelos":
"""
SELECT
model,
ROUND(AVG(avg_price_brl),2) AS Preco_Medio
FROM carros
GROUP BY model
ORDER BY Preco_Medio DESC
LIMIT 50;
"""
}

# ==================================
# EXPORTAÇÃO
# ==================================

try:

    conexao = sqlite3.connect(CAMINHO_BANCO)

    with pd.ExcelWriter(
        ARQUIVO_EXCEL,
        engine="openpyxl"
    ) as writer:

        for nome_planilha, consulta in consultas.items():

            print(f"Gerando: {nome_planilha}")

            df = pd.read_sql_query(
                consulta,
                conexao
            )

            df.to_excel(
                writer,
                sheet_name=nome_planilha,
                index=False
            )

    conexao.close()

    print("\n✅ Relatório criado com sucesso!")
    print(ARQUIVO_EXCEL)

except Exception as erro:

    print("Erro:")
    print(erro)