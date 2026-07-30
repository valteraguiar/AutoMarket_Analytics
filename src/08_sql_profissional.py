import sqlite3
import pandas as pd

# ==========================
# CONFIGURAÇÕES
# ==========================

CAMINHO_BANCO = "/storage/emulated/0/AutoMarket_Analytics/database.db"

# ==========================
# CONEXÃO
# ==========================

def conectar_banco():

    try:
        conexao = sqlite3.connect(CAMINHO_BANCO)
        print("✅ Banco conectado com sucesso.")
        return conexao

    except Exception as erro:
        print(f"❌ Erro ao conectar ao banco: {erro}")
        return None
        
def executar_consulta(conexao, titulo, consulta):

    try:

        resultado = pd.read_sql_query(consulta, conexao)

        print("\n" + "=" * 70)
        print(titulo)
        print("=" * 70)

        print(resultado)

        return resultado

    except Exception as erro:

        print(f"\n❌ Erro em '{titulo}'")
        print(erro)

        return None
        
def main():

    conexao = conectar_banco()

    if conexao is None:
        return

    consultas = {

        "TOP 10 MARCAS MAIS CARAS": """

        SELECT

            brand,

            ROUND(AVG(avg_price_brl),2) AS preco_medio

        FROM carros

        GROUP BY brand

        ORDER BY preco_medio DESC

        LIMIT 10

        """,

        "TOP 10 MARCAS MAIS PRESENTES": """

        SELECT

            brand,

            COUNT(*) AS quantidade

        FROM carros

        GROUP BY brand

        ORDER BY quantidade DESC

        LIMIT 10

        """,

        "PREÇO MÉDIO POR COMBUSTÍVEL": """

        SELECT

            fuel,

            COUNT(*) AS quantidade,

            ROUND(AVG(avg_price_brl),2) AS preco_medio

        FROM carros

        GROUP BY fuel

        ORDER BY preco_medio DESC

        """,

        "PREÇO MÉDIO POR CÂMBIO": """

        SELECT

            gear,

            COUNT(*) AS quantidade,

            ROUND(AVG(avg_price_brl),2) AS preco_medio

        FROM carros

        GROUP BY gear

        ORDER BY preco_medio DESC

        """
    }

    for titulo, consulta in consultas.items():

        executar_consulta(
            conexao,
            titulo,
            consulta
        )

    conexao.close()

    print("\n✅ Projeto finalizado.")
    
    