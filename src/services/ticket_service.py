import heapq

from models.ticket import Ticket
from repositories.ticket_repository import TicketRepository


class TicketService:

    def __init__(self, dados, cache=None):
        self.dados = dados
        self.cache = cache
        self.ticket_repository = TicketRepository()

    def tecnico_tem_competencia(self, id_tecnico, id_competencia):
        for relacao in self.dados["tecnico_competencia"]:
            if relacao[0] == id_tecnico and relacao[1] == id_competencia:
                return True

        return False

    def calcular_carga_tecnico(self, id_tecnico):
        carga = 0

        for ticket in self.dados["tickets"]:
            id_tecnico_ticket = ticket[7]
            estado = ticket[4]

            if id_tecnico_ticket == id_tecnico and estado != "FECHADO":
                carga += 1

        return carga

    def escolher_tecnico(self, id_competencia):
        fila_disponiveis = []
        fila_todos = []

        for tecnico in self.dados["tecnicos"]:
            id_tecnico = tecnico[0]
            disponivel = tecnico[3]
            ativo = tecnico[4]

            if ativo == 1 and self.tecnico_tem_competencia(id_tecnico, id_competencia):
                carga = self.calcular_carga_tecnico(id_tecnico)
                candidato = (
                    carga,
                    id_tecnico,
                    tecnico[1],
                    disponivel
                )

                heapq.heappush(fila_todos, candidato)

                if disponivel == 1:
                    heapq.heappush(fila_disponiveis, candidato)

        if fila_disponiveis:
            carga, id_tecnico, nome, disponivel = heapq.heappop(fila_disponiveis)
        elif fila_todos:
            carga, id_tecnico, nome, disponivel = heapq.heappop(fila_todos)
        else:
            return None

        return {
            "id_tecnico": id_tecnico,
            "nome": nome,
            "carga": carga,
            "disponivel": disponivel
        }

    def criar_ticket_com_atribuicao(self, titulo, descricao, prioridade, id_cliente, id_competencia):
        tecnico = self.escolher_tecnico(id_competencia)

        id_tecnico = None

        if tecnico:
            id_tecnico = tecnico["id_tecnico"]

        ticket = Ticket(
            titulo,
            descricao,
            prioridade,
            id_cliente,
            id_competencia,
            id_tecnico
        )

        self.ticket_repository.criar(ticket)

        if self.cache:
            self.cache.recarregar()
            self.dados = self.cache.obter_dados()
        else:
            self.dados["tickets"] = self.ticket_repository.listar()

        return tecnico
