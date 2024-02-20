# upgrade_manager.py
import pygame
from random import choice
from random import randint
import os

from upgrade import Upgrade

class Upgrade_Manager:
    def __init__(self, maze):
        self.color = (120, 120, 0)
        self.upgrade_block = pygame.sprite.Group()
        self.upgrade_ID = ''
        self.upgrade_choice = ['speed', 'fire rate']
        
        # Encontrar o caminho para a pasta Sprites
        current_path = os.path.dirname(__file__)
        sprite_path = os.path.join(current_path, 'Sprites')

        # Encontre todas as posições vazias no labirinto
        empty_positions = [(x, y) for y, row in enumerate(maze) for x, char in enumerate(row) if char == " "]
        if empty_positions:
            # Escolha uma posição aleatória entre as posições vazias
            x, y = empty_positions[randint(0, len(empty_positions) - 1)]
            # Crie o upgrade nessa posição
            upgrade_img = pygame.image.load(os.path.join(sprite_path, 'img_upgrade.png')).convert_alpha()
            upgrade = Upgrade(x, y, upgrade_img)
            print(upgrade)
            self.upgrade_ID = choice(self.upgrade_choice)

            self.upgrade_block.add(upgrade)

    def draw(self, screen):
        self.upgrade_block.draw(screen)
