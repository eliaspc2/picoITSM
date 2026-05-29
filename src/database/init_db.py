from db_connection import DatabaseConnection

conn = DatabaseConnection.ligar_bd()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tecnicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    disponivel INTEGER DEFAULT 1
)
""")

conn.commit()
DatabaseConnection.fechar_bd(conn)

print("Base de dados criada com sucesso.")