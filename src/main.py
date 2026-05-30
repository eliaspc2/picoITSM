from menus.menu import Menu
from database.init_db import criar_tabelas
from models.utilizador import Utilizador
from repositories.utilizador_repository import UtilizadorRepository


def main():
    criar_tabelas()

    utilizador_repository = UtilizadorRepository()
    utilizador_admin = Utilizador(
        "admin",
        "admin123",
        "ADMIN"
    )
    utilizador_repository.criar(utilizador_admin)

    menu = Menu()
    menu.mostrar_menu()


if __name__ == "__main__":
    main()
