import random

import pygame
import sys
from player import Player
from maze import Maze
from maze_list import MAZE_LIST

class Game:
    def __init__(self):
        pygame.init()

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        # Maze
        self.create_maze()

        #Players
        pygame.joystick.init()

        self.player = Player(self.screen, self.maze.walls,pygame.joystick.Joystick(0))

        # Groups
        self.bullet_group = pygame.sprite.Group()



    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((255, 255, 255))  # Fill the screen with white color
            self.player.player_commands()

            # draw groupss
            self.player.draw()
            self.bullet_group.update()
            self.bullet_group.draw(self.screen)
            self.maze.draw(self.screen)

            pygame.display.flip()
    def create_maze(self):
        self.maze = Maze(random.choice(MAZE_LIST))


if __name__ == "__main__":
    game = Game()
    game.start_game()
