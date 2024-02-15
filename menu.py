class Menu:
    def __init__(self):
        self.options = ["Play", "Credits"]
    
    def show_menu(self):
        print("=== MENU ===")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
    
    def choose_option(self):
        option = input("Choose an option: ")
        return int(option) - 1
    
    def show_credits(self):
        print("=== CREDITS ===")
        print("Team:")
        print("- João Lucas Noronha")
        print("- Juliana Ballin Lima")
        print("- Renato Barbosa")

    def start(self):
        while True:
            self.show_menu()
            choice = self.choose_option()

            if choice == 0:
                print("Starting the game...")
                # Start the game
            elif choice == 1:
                self.show_credits()
            else:
                print("Invalid option. Please choose again.")
