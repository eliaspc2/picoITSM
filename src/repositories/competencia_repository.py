from database.db_connection import DatabaseConnection


class CompetenciaRepository:

    def criar(self, competencia):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT OR IGNORE INTO competencias (nome, descricao)
                VALUES (?, ?)
            """, (
                competencia.nome,
                competencia.descricao
            ))

            conn.commit()
            if cursor.rowcount:
                print("Competência criada com sucesso.")
            else:
                print("Competência já existe.")

        except Exception as erro:
            print(f"Erro ao criar competência: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def listar(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, descricao
            FROM competencias
        """)

        competencias = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return competencias

    def atualizar(self, id_competencia, nome, descricao):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE competencias
                SET nome = ?, descricao = ?
                WHERE id = ?
            """, (nome, descricao, id_competencia))

            conn.commit()
            print("Competência atualizada com sucesso.")

        except Exception as erro:
            print(f"Erro ao atualizar competência: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def remover(self, id_competencia):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM competencias
                WHERE id = ?
            """, (id_competencia,))

            conn.commit()
            print("Competência removida com sucesso.")

        except Exception as erro:
            print(f"Erro ao remover competência: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)
