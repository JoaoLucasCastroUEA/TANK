import pygame
import sys
from player import Player

class Game:
    def __init__(self):
        pygame.init()

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")

        self.player = Player(self.screen)

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))  # Fill the screen with white color
            self.player.take_commands()
            self.player.draw()

            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.start_game()
