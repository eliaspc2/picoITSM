import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from services.ticket_service import TicketService


def criar_dados_teste():
    return {
        "utilizadores": [],
        "tecnicos": [
            (1, "João Silva", "joao@picoitsm.pt", 1, 1),
            (2, "Maria Santos", "maria@picoitsm.pt", 1, 1),
            (3, "Carlos Lima", "carlos@picoitsm.pt", 0, 1),
        ],
        "clientes": [],
        "competencias": [],
        "tecnico_competencia": [
            (1, 1),
            (2, 1),
            (3, 1),
        ],
        "tickets": [
            (1, "Ticket 1", "Descricao", "Alta", "ABERTO", 1, 1, 1, "Cliente", "Redes", "João Silva"),
            (2, "Ticket 2", "Descricao", "Media", "ABERTO", 1, 1, 1, "Cliente", "Redes", "João Silva"),
            (3, "Ticket 3", "Descricao", "Baixa", "ABERTO", 1, 1, 2, "Cliente", "Redes", "Maria Santos"),
            (4, "Ticket 4", "Descricao", "Baixa", "FECHADO", 1, 1, 2, "Cliente", "Redes", "Maria Santos"),
        ],
    }


class TestTicketService(unittest.TestCase):

    def test_tecnico_com_competencia_e_escolhido(self):
        dados = criar_dados_teste()
        service = TicketService(dados)

        tecnico = service.escolher_tecnico(1)

        self.assertIsNotNone(tecnico)
        self.assertIn(tecnico["id_tecnico"], [1, 2])

    def test_tecnico_com_menor_carga_e_escolhido(self):
        dados = criar_dados_teste()
        service = TicketService(dados)

        tecnico = service.escolher_tecnico(1)

        self.assertEqual(tecnico["id_tecnico"], 2)
        self.assertEqual(tecnico["carga"], 1)

    def test_sem_candidatos_retorna_none(self):
        dados = criar_dados_teste()
        service = TicketService(dados)

        tecnico = service.escolher_tecnico(99)

        self.assertIsNone(tecnico)


if __name__ == "__main__":
    unittest.main()
