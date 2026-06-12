from database.db_connection import DatabaseConnection
from models.utilizador import Utilizador
from utils.security import SecurityUtils
from utils.logger import Logger


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
                    ativo,
                    id_tecnico
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                utilizador.username,
                password_hash,
                utilizador.perfil,
                utilizador.ativo,
                utilizador.id_tecnico
            ))

            conn.commit()

            if cursor.rowcount:
                Logger.registar(
                    "CRIAR",
                    "utilizadores",
                    (
                        f"id={cursor.lastrowid}, username={utilizador.username}, "
                        f"perfil={utilizador.perfil}, id_tecnico={utilizador.id_tecnico}"
                    )
                )
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
                SELECT id, username, perfil, ativo, id_tecnico
                FROM utilizadores
            """)

            return cursor.fetchall()

        except Exception as erro:
            print(f"Erro ao listar utilizadores: {erro}")
            return []

        finally:
            DatabaseConnection.fechar_bd(conn)

    def atualizar(self, id_utilizador, username, perfil, ativo, id_tecnico=None):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE utilizadores
                SET username = ?,
                    perfil = ?,
                    ativo = ?,
                    id_tecnico = ?
                WHERE id = ?
            """, (
                username,
                perfil,
                ativo,
                id_tecnico,
                id_utilizador
            ))

            conn.commit()

            if cursor.rowcount:
                Logger.registar(
                    "ATUALIZAR",
                    "utilizadores",
                    (
                        f"id={id_utilizador}, username={username}, perfil={perfil}, "
                        f"ativo={ativo}, id_tecnico={id_tecnico}"
                    )
                )
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
                Logger.registar(
                    "REMOVER",
                    "utilizadores",
                    f"id={id_utilizador}"
                )
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

        try:
            cursor.execute("""
                SELECT id, username, password_hash, perfil, ativo, id_tecnico
                FROM utilizadores
                WHERE username = ?
                AND ativo = 1
            """, (username,))

            utilizador = cursor.fetchone()

            if utilizador and SecurityUtils.verificar_password(password, utilizador[2]):
                return (
                    utilizador[0],
                    utilizador[1],
                    utilizador[3],
                    utilizador[4],
                    utilizador[5]
                )

            return None

        except Exception as erro:
            print(f"Erro ao autenticar utilizador: {erro}")
            return None

        finally:
            DatabaseConnection.fechar_bd(conn)


def criar_utilizador(username, password, perfil, id_tecnico=None):
    utilizador = Utilizador(username, password, perfil, id_tecnico=id_tecnico)
    utilizador_repository = UtilizadorRepository()
    utilizador_repository.criar(utilizador)
