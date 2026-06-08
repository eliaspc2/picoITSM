import os
import subprocess
from getpass import getpass
from models.cliente import Cliente
from models.competencia import Competencia
from models.tecnico import Tecnico
from models.utilizador import Utilizador
from repositories.cliente_repository import ClienteRepository
from repositories.competencia_repository import CompetenciaRepository
from repositories.tecnico_repository import TecnicoRepository
from repositories.ticket_repository import TicketRepository
from repositories.utilizador_repository import UtilizadorRepository
from services.ticket_service import TicketService
from utils.validators import Validators


class Menu:
    def __init__(self, utilizador_atual, dados, cache=None):
        self.utilizador_atual = utilizador_atual
        self.dados = dados
        self.cache = cache
        self.tecnico_repository = TecnicoRepository()
        self.cliente_repository = ClienteRepository()
        self.competencia_repository = CompetenciaRepository()
        self.ticket_repository = TicketRepository()
        self.utilizador_repository = UtilizadorRepository()
        self.ticket_service = TicketService(dados, cache)

    @staticmethod
    def limpar_ecra():
        comando = "cls" if os.name == "nt" else "clear"
        subprocess.run(comando, shell=True, check=False)

    def desenhar_menu(self):
        print("\n=== picoITSM ===\n"
            "1. Técnicos\n"
            "2. Clientes\n"
            "3. Tickets\n"
            "4. Competências")

        if self.utilizador_atual[2] == "ADMIN":
            print("5. Utilizadores")

        print("0. Sair\n")

    def mostrar_menu(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print("\nVocê escolheu Técnicos.")
                self.menu_tecnicos()
            elif escolha == "2":
                print("\nVocê escolheu Clientes.")
                self.menu_clientes()
            elif escolha == "3":
                print("\nVocê escolheu Tickets.")
                self.menu_tickets()
            elif escolha == "4":
                print("\nVocê escolheu Competências.")
                self.menu_competencias()
            elif escolha == "5" and self.utilizador_atual[2] == "ADMIN":
                print("\nVocê escolheu Utilizadores.")
                self.menu_utilizadores()
            elif escolha == "0":
                print("\nSaindo do picoITSM. Até logo!\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")
    
# Menus específicos para cada entidade

    def desenhar_menu_tecnicos(self):
        print("\n=== Menu Técnicos ===\n"
        "1. Listar Técnicos\n" \
        "2. Adicionar Técnico\n" \
        "3. Editar Técnico\n" \
        "4. Excluir Técnico\n" \
        "0. Voltar ao Menu Principal\n")

    def desenhar_menu_clientes(self):
        print("\n=== Menu Clientes ===\n"
        "1. Listar Clientes\n" \
        "2. Adicionar Cliente\n" \
        "3. Editar Cliente\n" \
        "4. Excluir Cliente\n" \
        "0. Voltar ao Menu Principal\n")

    def desenhar_menu_tickets(self):
        print("\n=== Menu Tickets ===\n"
        "1. Listar Tickets\n" \
        "2. Adicionar Ticket\n" \
        "3. Editar Ticket\n" \
        "4. Excluir Ticket\n" \
        "0. Voltar ao Menu Principal\n")

    def desenhar_menu_competencias(self):
        print("\n=== Menu Competências ===\n"
        "1. Listar Competências\n" \
        "2. Adicionar Competência\n" \
        "3. Editar Competência\n" \
        "4. Excluir Competência\n" \
        "0. Voltar ao Menu Principal\n")

    def menu_tecnicos(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_tecnicos()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_tecnicos()
            elif escolha == "2":
                self.adicionar_tecnico()
            elif escolha == "3":
                self.editar_tecnico()
            elif escolha == "4":
                self.excluir_tecnico()
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def menu_clientes(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_clientes()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_clientes()
            elif escolha == "2":
                self.adicionar_cliente()
            elif escolha == "3":
                self.editar_cliente()
            elif escolha == "4":
                self.excluir_cliente()
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def menu_tickets(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_tickets()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_tickets()
            elif escolha == "2":
                self.adicionar_ticket()
            elif escolha == "3":
                self.editar_ticket()
            elif escolha == "4":
                self.excluir_ticket()
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def menu_competencias(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_competencias()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_competencias()
            elif escolha == "2":
                self.adicionar_competencia()
            elif escolha == "3":
                self.editar_competencia()
            elif escolha == "4":
                self.excluir_competencia()
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def listar_tecnicos(self):
        self.limpar_ecra()

        print("\n=== Lista de Técnicos ===\n")

        if not self.dados["tecnicos"]:
            print("Não existem técnicos registados.")
            input("\nPrima Enter para continuar...")
            return

        for tecnico in self.dados["tecnicos"]:
            disponivel = "Sim" if tecnico[3] == 1 else "Não"
            ativo = "Sim" if tecnico[4] == 1 else "Não"
            print(f"{tecnico[0]} - {tecnico[1]} | {tecnico[2]} | Disponível: {disponivel} | Ativo: {ativo}")

        input("\nPrima Enter para continuar...")

    def adicionar_tecnico(self):
        self.limpar_ecra()

        print("\n=== Adicionar Técnico ===\n")

        nome = self.ler_texto_obrigatorio("Nome: ")
        email = self.ler_email("Email: ")
        disponivel = self.ler_booleano("Disponível (1=Sim / 0=Não): ")
        ativo = self.ler_booleano("Ativo (1=Sim / 0=Não): ")

        tecnico = Tecnico(nome, email, disponivel, ativo)
        self.tecnico_repository.criar(tecnico)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def editar_tecnico(self):
        self.listar_tecnicos()
        self.limpar_ecra()

        print("\n=== Editar Técnico ===\n")

        id_tecnico = self.ler_id_existente("tecnicos", "ID do técnico: ")
        nome = self.ler_texto_obrigatorio("Nome: ")
        email = self.ler_email("Email: ")
        disponivel = self.ler_booleano("Disponível (1=Sim / 0=Não): ")
        ativo = self.ler_booleano("Ativo (1=Sim / 0=Não): ")

        self.tecnico_repository.atualizar(id_tecnico, nome, email, disponivel, ativo)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def excluir_tecnico(self):
        self.listar_tecnicos()
        self.limpar_ecra()

        print("\n=== Excluir Técnico ===\n")

        id_tecnico = self.ler_id_existente("tecnicos", "ID do técnico: ")
        self.tecnico_repository.remover(id_tecnico)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def listar_clientes(self):
        self.limpar_ecra()

        print("\n=== Lista de Clientes ===\n")

        if not self.dados["clientes"]:
            print("Não existem clientes registados.")
            input("\nPrima Enter para continuar...")
            return

        for cliente in self.dados["clientes"]:
            print(f"{cliente[0]} - {cliente[1]} | {cliente[2]} | {cliente[3]}")

        input("\nPrima Enter para continuar...")

    def adicionar_cliente(self):
        self.limpar_ecra()

        print("\n=== Adicionar Cliente ===\n")

        nome = self.ler_texto_obrigatorio("Nome: ")
        email = self.ler_email("Email: ")
        telefone = input("Telefone: ")

        cliente = Cliente(nome, email, telefone)
        self.cliente_repository.criar(cliente)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def editar_cliente(self):
        self.listar_clientes()
        self.limpar_ecra()

        print("\n=== Editar Cliente ===\n")

        id_cliente = self.ler_id_existente("clientes", "ID do cliente: ")
        nome = self.ler_texto_obrigatorio("Nome: ")
        email = self.ler_email("Email: ")
        telefone = input("Telefone: ")

        self.cliente_repository.atualizar(id_cliente, nome, email, telefone)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def excluir_cliente(self):
        self.listar_clientes()
        self.limpar_ecra()

        print("\n=== Excluir Cliente ===\n")

        id_cliente = self.ler_id_existente("clientes", "ID do cliente: ")
        self.cliente_repository.remover(id_cliente)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def listar_competencias(self):
        self.limpar_ecra()

        print("\n=== Lista de Competências ===\n")

        if not self.dados["competencias"]:
            print("Não existem competências registadas.")
            input("\nPrima Enter para continuar...")
            return

        for competencia in self.dados["competencias"]:
            print(f"{competencia[0]} - {competencia[1]} | {competencia[2]}")

        input("\nPrima Enter para continuar...")

    def adicionar_competencia(self):
        self.limpar_ecra()

        print("\n=== Adicionar Competência ===\n")

        nome = self.ler_texto_obrigatorio("Nome: ")
        descricao = input("Descrição: ")

        competencia = Competencia(nome, descricao)
        self.competencia_repository.criar(competencia)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def editar_competencia(self):
        self.listar_competencias()
        self.limpar_ecra()

        print("\n=== Editar Competência ===\n")

        id_competencia = self.ler_id_existente("competencias", "ID da competência: ")
        nome = self.ler_texto_obrigatorio("Nome: ")
        descricao = input("Descrição: ")

        self.competencia_repository.atualizar(id_competencia, nome, descricao)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def excluir_competencia(self):
        self.listar_competencias()
        self.limpar_ecra()

        print("\n=== Excluir Competência ===\n")

        id_competencia = self.ler_id_existente("competencias", "ID da competência: ")
        self.competencia_repository.remover(id_competencia)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def listar_tickets(self):
        self.limpar_ecra()

        print("\n=== Lista de Tickets ===\n")

        if not self.dados["tickets"]:
            print("Não existem tickets registados.")
            input("\nPrima Enter para continuar...")
            return

        for ticket in self.dados["tickets"]:
            tecnico = ticket[10] if ticket[10] else "Sem técnico"
            print(f"{ticket[0]} - {ticket[1]} | {ticket[3]} | {ticket[4]} | {tecnico}")

        input("\nPrima Enter para continuar...")

    def adicionar_ticket(self):
        self.limpar_ecra()

        print("\n=== Adicionar Ticket ===\n")

        titulo = self.ler_texto_obrigatorio("Título: ")
        descricao = self.ler_texto_obrigatorio("Descrição: ")
        prioridade = self.ler_prioridade("Prioridade (BAIXA/MEDIA/ALTA): ")

        print("\nClientes:")
        for cliente in self.dados["clientes"]:
            print(f"{cliente[0]} - {cliente[1]}")

        id_cliente = self.ler_id_existente("clientes", "\nID do cliente: ")

        print("\nCompetências:")
        for competencia in self.dados["competencias"]:
            print(f"{competencia[0]} - {competencia[1]}")

        id_competencia = self.ler_id_existente("competencias", "\nID da competência: ")

        tecnico = self.ticket_service.criar_ticket_com_atribuicao(
            titulo,
            descricao,
            prioridade,
            id_cliente,
            id_competencia
        )

        if tecnico:
            print(f"\nTicket atribuído automaticamente ao técnico: {tecnico['nome']}")
        else:
            print("\nTicket criado sem técnico atribuído.")

        input("\nPrima Enter para continuar...")

    def editar_ticket(self):
        self.listar_tickets()
        self.limpar_ecra()

        print("\n=== Editar Ticket ===\n")

        id_ticket = self.ler_id_existente("tickets", "ID do ticket: ")
        titulo = self.ler_texto_obrigatorio("Título: ")
        descricao = self.ler_texto_obrigatorio("Descrição: ")
        prioridade = self.ler_prioridade("Prioridade (BAIXA/MEDIA/ALTA): ")
        estado = self.ler_estado_ticket("Estado (ABERTO/EM_CURSO/FECHADO): ")

        print("\nClientes:")
        for cliente in self.dados["clientes"]:
            print(f"{cliente[0]} - {cliente[1]}")

        id_cliente = self.ler_id_existente("clientes", "\nID do cliente: ")

        print("\nCompetências:")
        for competencia in self.dados["competencias"]:
            print(f"{competencia[0]} - {competencia[1]}")

        id_competencia = self.ler_id_existente("competencias", "\nID da competência: ")

        print("\nTécnicos:")
        for tecnico in self.dados["tecnicos"]:
            print(f"{tecnico[0]} - {tecnico[1]}")

        id_tecnico = self.ler_id_tecnico_opcional("\nID do técnico (0 para sem técnico): ")

        self.ticket_repository.atualizar(
            id_ticket,
            titulo,
            descricao,
            prioridade,
            estado,
            id_cliente,
            id_competencia,
            id_tecnico
        )
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def excluir_ticket(self):
        self.listar_tickets()
        self.limpar_ecra()

        print("\n=== Excluir Ticket ===\n")

        id_ticket = self.ler_id_existente("tickets", "ID do ticket: ")
        self.ticket_repository.remover(id_ticket)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def ler_numero(self, mensagem):
        while True:
            valor = input(mensagem)

            if valor.isdigit():
                return int(valor)

            print("Valor inválido. Introduza um número.")

    def ler_numero_positivo(self, mensagem):
        while True:
            valor = input(mensagem)

            if Validators.inteiro_positivo(valor):
                return int(valor)

            print("Valor inválido. Introduza um número positivo.")

    def ler_booleano(self, mensagem):
        while True:
            valor = input(mensagem)

            if Validators.booleano_numero(valor):
                return int(valor)

            print("Valor inválido. Use 1 para Sim ou 0 para Não.")

    def ler_texto_obrigatorio(self, mensagem):
        while True:
            valor = input(mensagem)

            if Validators.nao_vazio(valor):
                return valor.strip()

            print("Valor obrigatório. Não pode ficar vazio.")

    def ler_email(self, mensagem):
        while True:
            valor = input(mensagem)

            if Validators.email(valor):
                return valor.strip()

            print("Email inválido.")

    def ler_prioridade(self, mensagem):
        while True:
            valor = input(mensagem).upper()

            if Validators.prioridade(valor):
                return valor

            print("Prioridade inválida. Use BAIXA, MEDIA ou ALTA.")

    def ler_estado_ticket(self, mensagem):
        while True:
            valor = input(mensagem).upper()

            if Validators.estado_ticket(valor):
                return valor

            print("Estado inválido. Use ABERTO, EM_CURSO ou FECHADO.")

    def ler_perfil_utilizador(self, mensagem):
        while True:
            valor = input(mensagem).upper()

            if valor in ["ADMIN", "TECNICO"]:
                return valor

            print("Perfil inválido. Use ADMIN ou TECNICO.")

    def existe_id(self, chave, id_registo):
        for registo in self.dados[chave]:
            if registo[0] == id_registo:
                return True

        return False

    def ler_id_existente(self, chave, mensagem):
        while True:
            id_registo = self.ler_numero_positivo(mensagem)

            if self.existe_id(chave, id_registo):
                return id_registo

            print("ID não encontrado.")

    def ler_id_tecnico_opcional(self, mensagem):
        while True:
            id_tecnico = self.ler_numero(mensagem)

            if id_tecnico == 0:
                return None

            if self.existe_id("tecnicos", id_tecnico):
                return id_tecnico

            print("ID de técnico não encontrado.")

    def desenhar_menu_utilizadores(self):
        print("\n=== Menu Utilizadores ===\n"
        "1. Listar Utilizadores\n"
        "2. Criar Administrador\n"
        "3. Criar Técnico\n"
        "4. Editar Utilizador\n"
        "5. Excluir Utilizador\n"
        "0. Voltar ao Menu Principal\n")


    def menu_utilizadores(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_utilizadores()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_utilizadores()
            elif escolha == "2":
                self.adicionar_administrador()
            elif escolha == "3":
                self.adicionar_utilizador_tecnico()
            elif escolha == "4":
                self.editar_utilizador()
            elif escolha == "5":
                self.excluir_utilizador()
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def adicionar_administrador(self):
        self.adicionar_utilizador_com_perfil("ADMIN")

    def adicionar_utilizador_tecnico(self):
        self.adicionar_utilizador_com_perfil("TECNICO")

    def adicionar_utilizador_com_perfil(self, perfil):
        self.limpar_ecra()

        print(f"\n=== Criar Utilizador {perfil} ===\n")

        username = self.ler_texto_obrigatorio("Username: ")
        password = getpass("Password: ")

        if not Validators.nao_vazio(password):
            print("\nPassword obrigatória.")
            input("\nPrima Enter para continuar...")
            return

        utilizador = Utilizador(username, password, perfil)
        self.utilizador_repository.criar(utilizador)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def listar_utilizadores(self):
        self.limpar_ecra()

        print("\n=== Lista de Utilizadores ===\n")

        if not self.dados["utilizadores"]:
            print("Não existem utilizadores registados.")
            input("\nPrima Enter para continuar...")
            return

        for utilizador in self.dados["utilizadores"]:
            ativo = "Sim" if utilizador[3] == 1 else "Não"
            print(f"{utilizador[0]} - {utilizador[1]} | {utilizador[2]} | Ativo: {ativo}")

        input("\nPrima Enter para continuar...")

    def editar_utilizador(self):
        self.listar_utilizadores()
        self.limpar_ecra()

        print("\n=== Editar Utilizador ===\n")

        id_utilizador = self.ler_id_existente("utilizadores", "ID do utilizador: ")
        username = self.ler_texto_obrigatorio("Username: ")
        perfil = self.ler_perfil_utilizador("Perfil (ADMIN/TECNICO): ")
        ativo = self.ler_booleano("Ativo (1=Sim / 0=Não): ")

        self.utilizador_repository.atualizar(id_utilizador, username, perfil, ativo)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def excluir_utilizador(self):
        self.listar_utilizadores()
        self.limpar_ecra()

        print("\n=== Excluir Utilizador ===\n")

        id_utilizador = self.ler_id_existente("utilizadores", "ID do utilizador: ")
        self.utilizador_repository.remover(id_utilizador)
        self.recarregar_dados()

        input("\nPrima Enter para continuar...")

    def recarregar_dados(self):
        if self.cache:
            self.cache.recarregar()
            self.dados = self.cache.obter_dados()
            self.ticket_service.dados = self.dados
