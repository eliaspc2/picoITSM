from database.db_connection import DatabaseConnection
from utils.logger import Logger


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
            Logger.registar(
                "CRIAR",
                "tickets",
                (
                    f"id={cursor.lastrowid}, titulo={ticket.titulo}, "
                    f"prioridade={ticket.prioridade}, estado={ticket.estado}, "
                    f"id_cliente={ticket.id_cliente}, id_competencia={ticket.id_competencia}, "
                    f"id_tecnico={ticket.id_tecnico}"
                )
            )
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
                tickets.id_cliente,
                tickets.id_competencia,
                tickets.id_tecnico,
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
            if cursor.rowcount:
                Logger.registar(
                    "ATUALIZAR",
                    "tickets",
                    (
                        f"id={id_ticket}, titulo={titulo}, prioridade={prioridade}, "
                        f"estado={estado}, id_cliente={id_cliente}, "
                        f"id_competencia={id_competencia}, id_tecnico={id_tecnico}"
                    )
                )
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
            if cursor.rowcount:
                Logger.registar(
                    "REMOVER",
                    "tickets",
                    f"id={id_ticket}"
                )
            print("Ticket removido com sucesso.")

        except Exception as erro:
            print(f"Erro ao remover ticket: {erro}")

        finally:
            DatabaseConnection.fechar_bd(conn)
