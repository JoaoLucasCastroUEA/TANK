import pygame
import sys
from maze import Maze
from maze_list import MAZE_LIST
from upgrade_manager import Upgrade_Manager
from player import Player
from sound_manager import Sound_Manager
import random

class Game:
    def __init__(self):
        pygame.init()

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Kombat")
        self.sound_manager = Sound_Manager()

        # Maze
        self.selected_maze = random.choice(MAZE_LIST)
        self.create_maze(self.width, self.height)
        self.create_upgrade()

        self.clock = pygame.time.Clock()

        # Bullet colors
        self.bullet_colors = [(0, 0, 255), (0, 255, 0)]

        # Load the background image
        self.bg_image = pygame.image.load("Sprites/img_bg_game.png").convert()

        # Players
        pygame.joystick.init()

        self.players = []

        if pygame.joystick.get_count() == 1:
            self.player1 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(0), (0, 255, 0), player_id=1,
                                  x=100, y=200)
            self.players.append(self.player1)
        elif pygame.joystick.get_count() == 2:
            self.player1 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(0), (0, 255, 0), player_id=1,
                                  x=100, y=200)
            self.player2 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(1), (0, 0, 255), player_id=2,
                                  x=1100, y=200)
            self.players.extend([self.player1, self.player2])
        elif pygame.joystick.get_count() == 3:
            self.player1 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(0), (0, 255, 0), player_id=1,
                                  x=100, y=200)
            self.player2 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(1), (0, 0, 255), player_id=2,
                                  x=1100, y=200)
            self.player3 = Player(self.screen, self.maze.walls, pygame.joystick.Joystick(2), (255, 0, 0), player_id=3,
                                  x=640, y=360)
            self.players.extend([self.player1, self.player2, self.player3])

        # Load the victory screen image
        self.victory_image = pygame.image.load("Sprites/img_bg_telavitoria.png").convert()

    def start_game(self):
        if pygame.joystick.get_count() < 2:
            # Se não houver pelo menos 2 joysticks conectados, exibe a tela de notificação de erro
            bg_telanotificacaoerro = pygame.image.load("Sprites/bg_telanotificacaoerro.png").convert()
            self.screen.blit(bg_telanotificacaoerro, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)  # Espera por 5 segundos
            pygame.quit()
            sys.exit()

        from player import Player
        
        self.sound_manager.play_game_music()

        while True:
            fps = self.clock.get_fps()
            print(f"FPS: {fps}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg_image, (0, 0))

            if len(self.upgrade.upgrade_block) == 0:
                self.create_upgrade()

            for player in self.players:
                player.Upgrade(self.upgrade, self.upgrade.upgrade_block)
                player.draw()

                # Check for collisions between current player's bullets and other players
                for player in self.players:
                    player.Upgrade(self.upgrade, self.upgrade.upgrade_block)
                    player.draw()

                    # Check for collisions between current player's bullets and other players
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
                            collisions = pygame.sprite.groupcollide(player.gun.bullets, other_player.gun.bullets, True,
                                                                    True)
                            for bullet in collisions:
                                print(
                                    f"Bullet collision between Player {player.player_id} and Player {other_player.player_id}!")
            self.maze.draw(self.screen)
            self.upgrade.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(1000)

            # Check if any player's life is zero
            if any(player.player_life <= 0 for player in self.players):
                self.display_victory_screen()
                break

    def create_maze(self, screen_width, screen_height):
        # Choose a random maze from MAZE_LIST
        self.maze = Maze(MAZE_LIST[0], screen_width, screen_height)
        
    def create_upgrade(self):
        self.upgrade = Upgrade_Manager(MAZE_LIST[0])

    def display_victory_screen(self):
        self.screen.blit(self.victory_image, (0, 0))

        # Get the winning player
        winning_player = next(player for player in self.players if player.player_life > 0)
        font = pygame.font.Font(None, 48)
        text_surface = font.render(f"Parabéns Jogador {winning_player.player_id}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2 ))  # Adjusted y position
        self.screen.blit(text_surface, text_rect)

        # Include a line after the text
        font = pygame.font.Font(None, 36)
        line_surface = font.render("Você foi o sobrevivente dessa batalha", True, (255, 255, 255))
        line_rect = line_surface.get_rect(center=(self.width // 2, text_rect.bottom + 25))  # Adjusted y position
        self.screen.blit(line_surface, line_rect)

        # Draw menu button
        menu_button = pygame.image.load("Sprites/img_menu_game.png").convert_alpha()
        menu_button_rect = menu_button.get_rect(center=(self.width // 2, 540))  # Adjusted y position
        self.screen.blit(menu_button, menu_button_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if menu_button_rect.collidepoint(mouse_pos):
                        # Go back to the menu
                        return

if __name__ == "__main__":
    game = Game()
    game.start_game()
