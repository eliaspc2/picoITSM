import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from database.db_connection import DatabaseConnection


def adicionar_coluna_se_nao_existir(cursor, tabela, coluna, definicao):
    cursor.execute(f"PRAGMA table_info({tabela})")
    colunas = [linha[1] for linha in cursor.fetchall()]

    if coluna not in colunas:
        cursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {definicao}")


def criar_tabelas():
    conn = DatabaseConnection.ligar_bd()
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            perfil TEXT NOT NULL,
            ativo INTEGER DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tecnicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            disponivel INTEGER DEFAULT 1,
            ativo INTEGER DEFAULT 1
        )
    """)

    adicionar_coluna_se_nao_existir(
        cursor,
        "tecnicos",
        "ativo",
        "INTEGER DEFAULT 1"
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefone TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tecnico_competencia (
            id_tecnico INTEGER NOT NULL,
            id_competencia INTEGER NOT NULL,
            PRIMARY KEY (id_tecnico, id_competencia),
            FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id),
            FOREIGN KEY (id_competencia) REFERENCES competencias(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'ABERTO',
            id_cliente INTEGER NOT NULL,
            id_competencia INTEGER NOT NULL,
            id_tecnico INTEGER,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id),
            FOREIGN KEY (id_competencia) REFERENCES competencias(id),
            FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id)
        )
    """)

    conn.commit()
    DatabaseConnection.fechar_bd(conn)


if __name__ == "__main__":
    criar_tabelas()
    print("Base de dados criada com sucesso.")
