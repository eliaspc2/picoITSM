from getpass import getpass
from time import sleep

from database.init_db import criar_tabelas
from menus.menu import Menu
from repositories.utilizador_repository import UtilizadorRepository


def login():
    Menu.limpar_ecra()
    utilizador_repository = UtilizadorRepository()

    while True:
        print("\n=== Login picoITSM ===")

        username = input("Username: ")
        password = getpass("Password: ")

        utilizador = utilizador_repository.autenticar(username, password)

        if utilizador:
            print(f"\nBem-vindo, {utilizador[1]}!")
            sleep(1)
            return utilizador

        print("\nUsername ou password inválidos.")


def main():
    criar_tabelas()
    
    menu = Menu(login())
    menu.mostrar_menu()


if __name__ == "__main__":
    main()
