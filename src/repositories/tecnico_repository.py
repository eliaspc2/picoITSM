from database.db_connection import DatabaseConnection


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
            print("Técnico removido com sucesso.")

        except Exception as erro:
            print(f"Erro ao remover técnico: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)
