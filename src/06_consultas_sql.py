import sqlite3
import pandas as pd

banco = "/storage/emulated/0/AutoMarket_Analytics/database.db"

conexao = sqlite3.connect(banco)

consulta = """
SELECT
    brand,
    ROUND(AVG(avg_price_brl),2) AS preco_medio
FROM carros
GROUP BY brand
ORDER BY preco_medio DESC
LIMIT 10;
"""

resultado = pd.read_sql_query(consulta, conexao)

print(resultado)

# Quantidade de veículos por marca
consulta = """ SELECT
    brand,
    COUNT(*) AS quantidade
FROM carros
GROUP BY brand
LIMIT 10;
"""
resultado = pd.read_sql_query(consulta, conexao)

print("\nTOP 10 MARCAS MAIS PRESENTES")
print(resultado)

# Preço médio por combustível
consulta = """
SELECT
    fuel,
    ROUND(AVG(avg_price_brl),2) AS preco
FROM carros
GROUP BY fuel
ORDER BY preco DESC
LIMIT 10;
"""
resultado = pd.read_sql_query(consulta, conexao)

print("\nTOP 10 MARCAS PREÇO MÉDIO POR COMBUSTÍVEL")
print(resultado)

# Preço médio por câmbio
consulta = """
SELECT
    gear,
    ROUND(AVG(avg_price_brl),2) AS preco
FROM carros
GROUP BY gear
ORDER BY preco DESC
LIMIT 10;
"""
resultado = pd.read_sql_query(consulta, conexao)

print("\nTOP 10 MARCAS PREÇO POR CÂMBIO")
print(resultado)

# Top 20 modelos mais caros
consulta = """
SELECT
    model,
    ROUND(AVG(avg_price_brl),2) AS preco
FROM carros
GROUP BY model
ORDER BY preco DESC
LIMIT 20;
"""

resultado = pd.read_sql_query(consulta, conexao)

print("\nTOP 20 MODELOS MAIS CAROS")
print(resultado)

# Evolução do preço médio por ano do modelo
consulta = """
SELECT
    year_model,
    ROUND(AVG(avg_price_brl),2) AS preco
FROM carros
GROUP BY year_model
ORDER BY year_model;
"""

resultado = pd.read_sql_query(consulta, conexao)

print("\nEVOLUCÃO DO PREÇO POR ANO")
print(resultado)

conexao.close( )