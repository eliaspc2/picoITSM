from models.ticket import Ticket

from repositories.ticket_repository import TicketRepository
from repositories.tecnico_repository import TecnicoRepository


class TicketService:

    def __init__(self):
        self.ticket_repository = TicketRepository()
        self.tecnico_repository = TecnicoRepository()

    def carregar_dados_memoria(self):
        tecnicos = self.tecnico_repository.listar()
        tickets = self.ticket_repository.listar()

        return tecnicos, tickets

    def calcular_carga_trabalho(self, id_tecnico):
        tickets = self.ticket_repository.listar()
        carga = 0

        for ticket in tickets:
            tecnico_nome = ticket[7]

            if tecnico_nome is not None:
                carga += 1

        return carga

    def procurar_tecnicos_disponiveis(self):
        tecnicos = self.tecnico_repository.listar()
        tecnicos_disponiveis = []

        for tecnico in tecnicos:
            disponivel = tecnico[3]
            ativo = tecnico[4]

            if disponivel == 1 and ativo == 1:
                tecnicos_disponiveis.append(tecnico)

        return tecnicos_disponiveis

    def escolher_tecnico_automaticamente(self):
        tecnicos_disponiveis = self.procurar_tecnicos_disponiveis()

        if not tecnicos_disponiveis:
            return None

        tecnico_escolhido = tecnicos_disponiveis[0]

        for tecnico in tecnicos_disponiveis:
            if tecnico[0] < tecnico_escolhido[0]:
                tecnico_escolhido = tecnico

        return tecnico_escolhido

    def criar_ticket_com_atribuicao(self, titulo, descricao, prioridade, id_cliente, id_competencia):
        tecnico = self.escolher_tecnico_automaticamente()

        id_tecnico = None

        if tecnico:
            id_tecnico = tecnico[0]

        ticket = Ticket(
            titulo,
            descricao,
            prioridade,
            id_cliente,
            id_competencia,
            id_tecnico
        )

        self.ticket_repository.criar(ticket)

        if tecnico:
            print(f"Ticket atribuído automaticamente ao técnico: {tecnico[1]}")
        else:
            print("Ticket criado sem técnico atribuído.")