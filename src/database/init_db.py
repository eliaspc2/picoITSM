from database.db_connection import DatabaseConnection


def criar_tabelas():
    conn = DatabaseConnection.ligar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            perfil TEXT NOT NULL,
            ativo INTEGER DEFAULT 1
        )
    """)

    conn.commit()
    DatabaseConnection.fechar_bd(conn)


if __name__ == "__main__":
    criar_tabelas()
    print("Base de dados criada com sucesso.")