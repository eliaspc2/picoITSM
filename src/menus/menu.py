class Menu:

    def __init__(self):
        self.mostrar_menu()

    def desenhar_menu():
        print("\n=== picoITSM ===\n" \
        "1. Técnicos\n" \
        "2. Clientes\n" \
        "3. Tickets\n" \
        "0. Sair\n")


    def mostrar_menu():
        while True:
            self.desenhar_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print("Você escolheu Técnicos.")
                # Aqui você pode chamar a função para gerenciar técnicos
            elif escolha == "2":
                print("Você escolheu Clientes.")
                # Aqui você pode chamar a função para gerenciar clientes
            elif escolha == "3":
                print("Você escolheu Tickets.")
                # Aqui você pode chamar a função para gerenciar tickets
            elif escolha == "0":
                print("Saindo do picoITSM. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")