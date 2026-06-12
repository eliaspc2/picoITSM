from getpass import getpass
from time import sleep

from database.init_db import criar_tabelas
from menus.menu import Menu
from repositories.utilizador_repository import UtilizadorRepository
from services.memory_cache import MemoryCache
from utils.logger import Logger


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

    cache = MemoryCache()
    cache.carregar()

    cache.resumo()

    dados = cache.obter_dados()

    utilizador_atual = login()
    Logger.definir_utilizador(utilizador_atual)

    menu = Menu(utilizador_atual, dados, cache)
    menu.mostrar_menu()


if __name__ == "__main__":
    main()
