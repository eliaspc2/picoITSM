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

    def listar(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT id, username, perfil, ativo
                FROM utilizadores
            """)

            return cursor.fetchall()

        except Exception as erro:
            print(f"Erro ao listar utilizadores: {erro}")
            return []

        finally:
            DatabaseConnection.fechar_bd(conn)

    def atualizar(self, id_utilizador, username, perfil, ativo):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE utilizadores
                SET username = ?,
                    perfil = ?,
                    ativo = ?
                WHERE id = ?
            """, (
                username,
                perfil,
                ativo,
                id_utilizador
            ))

            conn.commit()

            if cursor.rowcount:
                print("Utilizador atualizado com sucesso.")
            else:
                print("Utilizador não encontrado.")

        except Exception as erro:
            print(f"Erro ao atualizar utilizador: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def remover(self, id_utilizador):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM utilizadores
                WHERE id = ?
            """, (id_utilizador,))

            conn.commit()

            if cursor.rowcount:
                print("Utilizador removido com sucesso.")
            else:
                print("Utilizador não encontrado.")

        except Exception as erro:
            print(f"Erro ao remover utilizador: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def autenticar(self, username, password):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        password_hash = SecurityUtils.gerar_hash(password)

        try:
            cursor.execute("""
                SELECT id, username, perfil, ativo
                FROM utilizadores
                WHERE username = ?
                AND password_hash = ?
                AND ativo = 1
            """, (
                username,
                password_hash
            ))

            return cursor.fetchone()

        except Exception as erro:
            print(f"Erro ao autenticar utilizador: {erro}")
            return None

        finally:
            DatabaseConnection.fechar_bd(conn)


def criar_utilizador(username, password, perfil):
    utilizador = Utilizador(username, password, perfil)
    utilizador_repository = UtilizadorRepository()
    utilizador_repository.criar(utilizador)