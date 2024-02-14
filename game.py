import random
import pygame
import sys
from player import Player
from maze import Maze
from maze_list import MAZE_LIST
from upgrade_manager import Upgrade_Manager


class Game:
    def __init__(self):
        pygame.init()

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")

        # Maze
        self.create_maze()
        self.create_upgrade()


        # Bullet colors
        self.bullet_colors = [(0, 0, 255), (0, 255, 0)]

        # Players
        pygame.joystick.init()

        self.players = []

        if pygame.joystick.get_count() == 1:
            self.player1 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(0), (0, 255, 0), player_id=1)
            self.players.append(self.player1)
        elif pygame.joystick.get_count() == 2:
            self.player1 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(0), (0, 255, 0), player_id=1)
            self.player2 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(1), (0, 0, 255), player_id=2)
            self.players.extend([self.player1, self.player2])

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((255, 255, 255))
            if len(self.upgrade.upgrade_block) == 0:
                self.create_upgrade()
            for player in self.players:
                player.Upgrade(self.upgrade, self.upgrade.upgrade_block)
                player.draw()

                # Verifica colisões entre as balas do jogador atual e os outros jogadores
                for other_player in self.players:
                    if other_player.player_id != player.player_id and player.player_life > 0:
                        collisions = pygame.sprite.spritecollide(player, other_player.gun.bullets, True)
                        for bullet in collisions:
                            print(f"Player {player.player_id} hit by Player {other_player.player_id}'s bullet!")
                            player.player_life -= 1
                            print(f"Player {other_player.player_id} life = {other_player.player_life}")

                for other_player in self.players:
                    if other_player.player_id != player.player_id and player.player_life > 0:
                        # Player-to-Player Bullet Collision
                        collisions = pygame.sprite.groupcollide(player.gun.bullets, other_player.gun.bullets, True, True)
                        for bullet in collisions:
                            print(
                                f"Bullet collision between Player {player.player_id} and Player {other_player.player_id}!")

            self.maze.draw(self.screen)
            self.upgrade.draw(self.screen)

            pygame.display.flip()

    def create_maze(self):
        self.maze = Maze(MAZE_LIST[0])

    def create_upgrade(self):
        self.upgrade = Upgrade_Manager(MAZE_LIST[0])


if __name__ == "__main__":
    game = Game()
    game.start_game()
