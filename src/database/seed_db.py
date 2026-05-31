import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from database.db_connection import DatabaseConnection
from database.init_db import criar_tabelas

from models.utilizador import Utilizador
from models.tecnico import Tecnico
from models.cliente import Cliente
from models.competencia import Competencia
from models.ticket import Ticket

from repositories.utilizador_repository import UtilizadorRepository
from repositories.tecnico_repository import TecnicoRepository
from repositories.cliente_repository import ClienteRepository
from repositories.competencia_repository import CompetenciaRepository
from repositories.ticket_repository import TicketRepository


def obter_id_por_nome(tabela, nome):
    conn = DatabaseConnection.ligar_bd()
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT id
        FROM {tabela}
        WHERE nome = ?
    """, (nome,))

    resultado = cursor.fetchone()
    DatabaseConnection.fechar_bd(conn)

    if resultado:
        return resultado[0]

    return None


def associar_tecnico_competencia(id_tecnico, id_competencia):
    conn = DatabaseConnection.ligar_bd()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT OR IGNORE INTO tecnico_competencia (
                id_tecnico,
                id_competencia
            )
            VALUES (?, ?)
        """, (
            id_tecnico,
            id_competencia
        ))

        conn.commit()

    except Exception as erro:
        print(f"Erro ao associar técnico a competência: {erro}")

    finally:
        DatabaseConnection.fechar_bd(conn)


def seed():
    criar_tabelas()

    utilizador_repository = UtilizadorRepository()
    tecnico_repository = TecnicoRepository()
    cliente_repository = ClienteRepository()
    competencia_repository = CompetenciaRepository()
    ticket_repository = TicketRepository()

    print("A criar dados de teste...")

    utilizador_repository.criar(
        Utilizador("admin", "admin123", "ADMIN")
    )

    utilizador_repository.criar(
        Utilizador("joao", "joao123", "TECNICO")
    )

    utilizador_repository.criar(
        Utilizador("maria", "maria123", "TECNICO")
    )

    tecnico_repository.criar(
        Tecnico("João Silva", "joao@picoitsm.pt")
    )

    tecnico_repository.criar(
        Tecnico("Maria Santos", "maria@picoitsm.pt")
    )

    cliente_repository.criar(
        Cliente("Empresa Alpha", "geral@alpha.pt", "912345678")
    )

    cliente_repository.criar(
        Cliente("Empresa Beta", "geral@beta.pt", "923456789")
    )

    competencia_repository.criar(
        Competencia("Redes", "Administração e suporte de redes")
    )

    competencia_repository.criar(
        Competencia("Hardware", "Diagnóstico e reparação de hardware")
    )

    competencia_repository.criar(
        Competencia("Software", "Instalação e suporte de aplicações")
    )

    id_joao = obter_id_por_nome("tecnicos", "João Silva")
    id_maria = obter_id_por_nome("tecnicos", "Maria Santos")

    id_redes = obter_id_por_nome("competencias", "Redes")
    id_hardware = obter_id_por_nome("competencias", "Hardware")
    id_software = obter_id_por_nome("competencias", "Software")

    id_alpha = obter_id_por_nome("clientes", "Empresa Alpha")
    id_beta = obter_id_por_nome("clientes", "Empresa Beta")

    associar_tecnico_competencia(id_joao, id_redes)
    associar_tecnico_competencia(id_joao, id_hardware)
    associar_tecnico_competencia(id_maria, id_software)
    associar_tecnico_competencia(id_maria, id_redes)

    ticket_repository.criar(
        Ticket(
            "Sem acesso à rede",
            "O cliente não consegue aceder à rede interna.",
            "Alta",
            id_alpha,
            id_redes,
            id_joao
        )
    )

    ticket_repository.criar(
        Ticket(
            "Erro na aplicação",
            "A aplicação principal apresenta erro ao iniciar.",
            "Média",
            id_beta,
            id_software,
            id_maria
        )
    )

    print("Dados de teste criados.")


if __name__ == "__main__":
    seed()