from database.db_connection import DatabaseConnection


class ClienteRepository:

    def criar(self, cliente):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT OR IGNORE INTO clientes (nome, email, telefone)
                VALUES (?, ?, ?)
            """, (
                cliente.nome,
                cliente.email,
                cliente.telefone
            ))

            conn.commit()
            if cursor.rowcount:
                print("Cliente criado com sucesso.")
            else:
                print("Cliente já existe.")

        except Exception as erro:
            print(f"Erro ao criar cliente: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def listar(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, email, telefone
            FROM clientes
        """)

        clientes = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return clientes

    def atualizar(self, id_cliente, nome, email, telefone):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE clientes
                SET nome = ?, email = ?, telefone = ?
                WHERE id = ?
            """, (nome, email, telefone, id_cliente))

            conn.commit()
            print("Cliente atualizado com sucesso.")

        except Exception as erro:
            print(f"Erro ao atualizar cliente: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def remover(self, id_cliente):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM clientes
                WHERE id = ?
            """, (id_cliente,))

            conn.commit()
            print("Cliente removido com sucesso.")

        except Exception as erro:
            print(f"Erro ao remover cliente: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)
