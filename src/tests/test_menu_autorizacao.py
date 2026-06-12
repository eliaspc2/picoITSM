import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from menus.menu import Menu


def criar_dados_tickets():
    return {
        "utilizadores": [],
        "tecnicos": [
            (1, "João Silva", "joao@picoitsm.pt", 1, 1),
            (2, "Maria Santos", "maria@picoitsm.pt", 1, 1),
        ],
        "clientes": [],
        "competencias": [],
        "tecnico_competencia": [],
        "tickets": [
            (1, "Ticket João", "Descricao", "Alta", "ABERTO", 1, 1, 1, "Cliente", "Redes", "João Silva"),
            (2, "Ticket Maria", "Descricao", "Media", "ABERTO", 1, 1, 2, "Cliente", "Redes", "Maria Santos"),
            (3, "Sem técnico", "Descricao", "Baixa", "ABERTO", 1, 1, None, "Cliente", "Redes", None),
        ],
    }


class TestMenuAutorizacao(unittest.TestCase):

    def test_admin_ve_todos_os_tickets(self):
        menu = Menu((1, "admin", "ADMIN", 1, None), criar_dados_tickets())

        tickets = menu.obter_tickets_visiveis()

        self.assertEqual(len(tickets), 3)

    def test_tecnico_ve_apenas_os_seus_tickets(self):
        menu = Menu((2, "user", "TECNICO", 1, 1), criar_dados_tickets())

        tickets = menu.obter_tickets_visiveis()

        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0][0], 1)

    def test_tecnico_sem_ligacao_nao_ve_tickets(self):
        menu = Menu((3, "sem_tecnico", "TECNICO", 1, None), criar_dados_tickets())

        tickets = menu.obter_tickets_visiveis()

        self.assertEqual(tickets, [])


if __name__ == "__main__":
    unittest.main()
