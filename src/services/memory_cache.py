from repositories.utilizador_repository import UtilizadorRepository
from repositories.tecnico_repository import TecnicoRepository
from repositories.cliente_repository import ClienteRepository
from repositories.competencia_repository import CompetenciaRepository
from repositories.ticket_repository import TicketRepository
from database.db_connection import DatabaseConnection


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
            "tecnico_competencia": [],
            "tickets": []
        }

    def carregar(self):
        self.dados["utilizadores"] = self.utilizador_repository.listar()
        self.dados["tecnicos"] = self.tecnico_repository.listar()
        self.dados["clientes"] = self.cliente_repository.listar()
        self.dados["competencias"] = self.competencia_repository.listar()
        self.dados["tecnico_competencia"] = self.carregar_tecnico_competencia()
        self.dados["tickets"] = self.ticket_repository.listar()

    def carregar_tecnico_competencia(self):
        conn = DatabaseConnection.ligar_bd()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_tecnico, id_competencia
            FROM tecnico_competencia
        """)

        relacoes = cursor.fetchall()
        DatabaseConnection.fechar_bd(conn)

        return relacoes

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
