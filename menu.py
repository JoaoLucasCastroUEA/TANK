import pygame
import os
from credits import Credits
from game import Game  # Importe a classe Game

class Menu:
    def __init__(self):
        self.options = ["Play", "Credits"]
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(os.path.join("Sprites", "img_bg_menu.png")).convert()
        self.play_button = pygame.image.load(os.path.join("Sprites", "img_play_menu.png")).convert_alpha()
        self.credit_button = pygame.image.load(os.path.join("Sprites", "img_credits_menu.png")).convert_alpha()

    def show_menu(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.play_button, (self.width // 2 - self.play_button.get_width() // 2, 435))
        self.screen.blit(self.credit_button, (self.width // 2 - self.credit_button.get_width() // 2, 535))
        pygame.display.flip()

    def choose_option(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.width // 2 - self.play_button.get_width() // 2 <= mouse_pos[0] <= self.width // 2 + self.play_button.get_width() // 2 \
                            and 435 <= mouse_pos[1] <= 435 + self.play_button.get_height():
                        return "play"
                    elif self.width // 2 - self.credit_button.get_width() // 2 <= mouse_pos[0] <= self.width // 2 + self.credit_button.get_width() // 2 \
                            and 535 <= mouse_pos[1] <= 535 + self.credit_button.get_height():
                        return "credits"

    def start(self):
        pygame.init()
        pygame.display.set_caption('Mazer Kombat')

        menu_music_file_path = 'Sounds/Music/menumusic.wav'
        pygame.mixer.music.load(menu_music_file_path)
        pygame.mixer.music.play(loops=-1)

        running = True
        while running:
            self.show_menu()
            choice = self.choose_option()

            if choice == "play":
                print("Starting the game...")
                game = Game()  # Remove a passagem de self.screen como argumento
                game.start_game()  # Inicia o jogo


            elif choice == "credits":
                credits = Credits(self.screen, self.width, self.height)
                credits.show_credits()
