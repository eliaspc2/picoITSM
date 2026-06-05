from repositories.utilizador_repository import UtilizadorRepository
from repositories.tecnico_repository import TecnicoRepository
from repositories.cliente_repository import ClienteRepository
from repositories.competencia_repository import CompetenciaRepository
from repositories.ticket_repository import TicketRepository


class MemoryCache:

    def __init__(self):
        self.utilizador_repository = UtilizadorRepository()
        self.tecnico_repository = TecnicoRepository()
        self.cliente_repository = ClienteRepository()
        self.competencia_repository = CompetenciaRepository()
        self.ticket_repository = TicketRepository()

        self.dados = {
            "utilizadores": [],
            "tecnicos": [],
            "clientes": [],
            "competencias": [],
            "tickets": []
        }

    def carregar(self):
        self.dados["utilizadores"] = self.utilizador_repository.listar()
        self.dados["tecnicos"] = self.tecnico_repository.listar()
        self.dados["clientes"] = self.cliente_repository.listar()
        self.dados["competencias"] = self.competencia_repository.listar()
        self.dados["tickets"] = self.ticket_repository.listar()

    def limpar(self):
        for chave in self.dados:
            self.dados[chave].clear()

    def recarregar(self):
        self.limpar()
        self.carregar()

    def obter_dados(self):
        return self.dados

    def obter(self, chave):
        return self.dados.get(chave, [])

    def resumo(self):
        print("\n=== Cache de Memória ===\n")

        for chave, valor in self.dados.items():
            print(f"{chave}: {len(valor)}")
