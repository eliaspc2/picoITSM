from database.db_connection import DatabaseConnection
from utils.logger import Logger


class TecnicoCompetenciaRepository:

    def associar(self, id_tecnico, id_competencia):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT OR IGNORE INTO tecnico_competencia (
                    id_tecnico,
                    id_competencia
                )
                VALUES (?, ?)
            """, (
                id_tecnico,
                id_competencia
            ))

            conn.commit()

            if cursor.rowcount:
                Logger.registar(
                    "ASSOCIAR",
                    "tecnico_competencia",
                    f"id_tecnico={id_tecnico}, id_competencia={id_competencia}"
                )
                print("Competência associada ao técnico com sucesso.")
            else:
                print("Essa competência já está associada ao técnico.")

        except Exception as erro:
            print(f"Erro ao associar competência ao técnico: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def remover(self, id_tecnico, id_competencia):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM tecnico_competencia
                WHERE id_tecnico = ?
                AND id_competencia = ?
            """, (
                id_tecnico,
                id_competencia
            ))

            conn.commit()

            if cursor.rowcount:
                Logger.registar(
                    "REMOVER",
                    "tecnico_competencia",
                    f"id_tecnico={id_tecnico}, id_competencia={id_competencia}"
                )
                print("Competência removida do técnico com sucesso.")
            else:
                print("Associação não encontrada.")

        except Exception as erro:
            print(f"Erro ao remover competência do técnico: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def listar(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_tecnico, id_competencia
            FROM tecnico_competencia
        """)

        relacoes = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return relacoes

    def listar_por_tecnico(self, id_tecnico):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_tecnico, id_competencia
            FROM tecnico_competencia
            WHERE id_tecnico = ?
        """, (id_tecnico,))

        relacoes = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return relacoes
