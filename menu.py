class Menu:
    def __init__(self):
        self.opcoes = ["Play", "Créditos"]
    
    def exibir_menu(self):
        print("=== MENU ===")
        for i, opcao in enumerate(self.opcoes, start=1):
            print(f"{i}. {opcao}")
    
    def escolher_opcao(self):
        opcao = input("Escolha uma opção: ")
        return int(opcao) - 1
    
    def exibir_creditos(self):
        print("=== CRÉDITOS ===")
        print("Equipe:")
        print("- João Lucas Noronha")
        print("- Juliana Ballin Lima")
        print("- Renato Barbosa")

    def iniciar(self):
        while True:
            self.exibir_menu()
            escolha = self.escolher_opcao()

            if escolha == 0:
                print("Iniciando o jogo...")
                # Iniciar o jogo
            elif escolha == 1:
                self.exibir_creditos()
            else:
                print("Opção inválida. Escolha novamente.")
