from database.db_connection import DatabaseConnection


class TicketRepository:

    def criar(self, ticket):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO tickets (
                    titulo,
                    descricao,
                    prioridade,
                    estado,
                    id_cliente,
                    id_competencia,
                    id_tecnico
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                ticket.titulo,
                ticket.descricao,
                ticket.prioridade,
                ticket.estado,
                ticket.id_cliente,
                ticket.id_competencia,
                ticket.id_tecnico
            ))

            conn.commit()
            print("Ticket criado com sucesso.")

        except Exception as erro:
            print(f"Erro ao criar ticket: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def listar(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                tickets.id,
                tickets.titulo,
                tickets.descricao,
                tickets.prioridade,
                tickets.estado,
                clientes.nome,
                competencias.nome,
                tecnicos.nome
            FROM tickets
            JOIN clientes ON tickets.id_cliente = clientes.id
            JOIN competencias ON tickets.id_competencia = competencias.id
            LEFT JOIN tecnicos ON tickets.id_tecnico = tecnicos.id
        """)

        tickets = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return tickets

    def atualizar(self, id_ticket, titulo, descricao, prioridade, estado, id_cliente, id_competencia, id_tecnico):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                UPDATE tickets
                SET titulo = ?,
                    descricao = ?,
                    prioridade = ?,
                    estado = ?,
                    id_cliente = ?,
                    id_competencia = ?,
                    id_tecnico = ?
                WHERE id = ?
            """, (
                titulo,
                descricao,
                prioridade,
                estado,
                id_cliente,
                id_competencia,
                id_tecnico,
                id_ticket
            ))

            conn.commit()
            print("Ticket atualizado com sucesso.")

        except Exception as erro:
            print(f"Erro ao atualizar ticket: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)

    def remover(self, id_ticket):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                DELETE FROM tickets
                WHERE id = ?
            """, (id_ticket,))

            conn.commit()
            print("Ticket removido com sucesso.")

        except Exception as erro:
            print(f"Erro ao remover ticket: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)