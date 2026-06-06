import os
import subprocess
from getpass import getpass
from models.utilizador import Utilizador
from repositories.utilizador_repository import UtilizadorRepository
from services.ticket_service import TicketService

class Menu:
    def __init__(self, utilizador_atual, dados, cache=None):
        self.utilizador_atual = utilizador_atual
        self.dados = dados
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
            "3. Tickets")

        if self.utilizador_atual[2] == "ADMIN":
            print("4. Utilizadores")

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
            elif escolha == "4" and self.utilizador_atual[2] == "ADMIN":
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

    def menu_tecnicos(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_tecnicos()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print("\nVocê escolheu Listar Técnicos.")
            elif escolha == "2":
                print("\nVocê escolheu Adicionar Técnico.")
            elif escolha == "3":
                print("\nVocê escolheu Editar Técnico.")
            elif escolha == "4":
                print("\nVocê escolheu Excluir Técnico.")
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
                print("\nVocê escolheu Listar Clientes.")
            elif escolha == "2":
                print("\nVocê escolheu Adicionar Cliente.")
            elif escolha == "3":
                print("\nVocê escolheu Editar Cliente.")
            elif escolha == "4":
                print("\nVocê escolheu Excluir Cliente.")
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
                print("\nVocê escolheu Editar Ticket.")
            elif escolha == "4":
                print("\nVocê escolheu Excluir Ticket.")
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

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

        titulo = input("Título: ")
        descricao = input("Descrição: ")
        prioridade = input("Prioridade (Baixa/Média/Alta): ")

        print("\nClientes:")
        for cliente in self.dados["clientes"]:
            print(f"{cliente[0]} - {cliente[1]}")

        id_cliente = self.ler_numero("\nID do cliente: ")

        print("\nCompetências:")
        for competencia in self.dados["competencias"]:
            print(f"{competencia[0]} - {competencia[1]}")

        id_competencia = self.ler_numero("\nID da competência: ")

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

    def ler_numero(self, mensagem):
        while True:
            valor = input(mensagem)

            if valor.isdigit():
                return int(valor)

            print("Valor inválido. Introduza um número.")

    def desenhar_menu_utilizadores(self):
        print("\n=== Menu Utilizadores ===\n"
        "1. Adicionar Utilizador\n"
        "0. Voltar ao Menu Principal\n")


    def menu_utilizadores(self):
        while True:
            self.limpar_ecra()
            self.desenhar_menu_utilizadores()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.adicionar_utilizador()
            elif escolha == "0":
                print("\nVoltando ao Menu Principal.\n")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def adicionar_utilizador(self):
        self.limpar_ecra()

        print("\n=== Adicionar Utilizador ===\n")

        username = input("Username: ")
        password = getpass("Password: ")
        perfil = input("Perfil (ADMIN/TECNICO): ").upper()

        if perfil not in ["ADMIN", "TECNICO"]:
            print("\nPerfil inválido.")
            input("\nPrima Enter para continuar...")
            return

        utilizador = Utilizador(username, password, perfil)
        self.utilizador_repository.criar(utilizador)

        input("\nPrima Enter para continuar...")
