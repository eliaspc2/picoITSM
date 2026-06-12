from database.db_connection import DatabaseConnection
from utils.logger import Logger


class TecnicoRepository:

    def criar(self, tecnico):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT OR IGNORE INTO tecnicos (nome, email, disponivel, ativo)
                VALUES (?, ?, ?, ?)
            """, (
                tecnico.nome,
                tecnico.email,
                tecnico.disponivel,
                tecnico.ativo
            ))

            conn.commit()
            if cursor.rowcount:
                Logger.registar(
                    "CRIAR",
                    "tecnicos",
                    f"id={cursor.lastrowid}, nome={tecnico.nome}, email={tecnico.email}"
                )
                print("Técnico criado com sucesso.")
            else:
                print("Técnico já existe.")

        except Exception as erro:
            print(f"Erro ao criar técnico: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def listar(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email, disponivel, ativo
            FROM tecnicos
        """)

        tecnicos = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return tecnicos

    def obter_por_email(self, email):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email, disponivel, ativo
            FROM tecnicos
            WHERE email = ?
        """, (email,))

        tecnico = cursor.fetchone()
        DatabaseConnection.fechar_bd(conn)

        return tecnico

    def atualizar(self, id_tecnico, nome, email, disponivel, ativo):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE tecnicos
                SET nome = ?, email = ?, disponivel = ?, ativo = ?
                WHERE id = ?
            """, (nome, email, disponivel, ativo, id_tecnico))

            conn.commit()
            if cursor.rowcount:
                Logger.registar(
                    "ATUALIZAR",
                    "tecnicos",
                    f"id={id_tecnico}, nome={nome}, email={email}, disponivel={disponivel}, ativo={ativo}"
                )
            print("Técnico atualizado com sucesso.")

        except Exception as erro:
            print(f"Erro ao atualizar técnico: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def remover(self, id_tecnico):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM tecnicos
                WHERE id = ?
            """, (id_tecnico,))

            conn.commit()
            if cursor.rowcount:
                Logger.registar(
                    "REMOVER",
                    "tecnicos",
                    f"id={id_tecnico}"
                )
            print("Técnico removido com sucesso.")

        except Exception as erro:
            print(f"Erro ao remover técnico: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)
