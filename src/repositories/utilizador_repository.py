from database.db_connection import DatabaseConnection
from models.utilizador import Utilizador
from utils.security import SecurityUtils


class UtilizadorRepository:
    def criar(self, utilizador):

        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        password_hash = SecurityUtils.gerar_hash(utilizador.password)

        try:

            cursor.execute("""
                INSERT OR IGNORE INTO utilizadores (
                    username,
                    password_hash,
                    perfil,
                    ativo
                )
                VALUES (?, ?, ?, ?)
            """, (
                utilizador.username,
                password_hash,
                utilizador.perfil,
                utilizador.ativo
            ))

            conn.commit()

            if cursor.rowcount:
                print("Utilizador criado com sucesso.")
            else:
                print("Utilizador já existe.")

        except Exception as erro:

            print(f"Erro ao criar utilizador: {erro}")

        finally:

            DatabaseConnection.fechar_bd(conn)


def criar_utilizador(username, password, perfil):
    utilizador = Utilizador(username, password, perfil)
    utilizador_repository = UtilizadorRepository()
    utilizador_repository.criar(utilizador)
