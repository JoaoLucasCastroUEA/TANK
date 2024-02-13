import random

import pygame
from upgrade import Upgrade
from random import randint

class Upgrade_Manager:
    def __init__(self, maze):
        self.color = (120, 120, 0)
        self.upgrade_block = pygame.sprite.Group()
        self.upgrade_ID = ''
        self.upgrade_choice = ['speed','fire rate']

        # Encontre todas as posições vazias no labirinto
        empty_positions = [(x, y) for y, row in enumerate(maze) for x, char in enumerate(row) if char == " "]

        if empty_positions:
            # Escolha uma posição aleatória entre as posições vazias
            x, y = empty_positions[randint(0, len(empty_positions) - 1)]

            # Crie o upgrade nessa posição
            upgrade = Upgrade(x,y,self.color)
            self.upgrade_ID = random.choice(self.upgrade_choice)

            self.upgrade_block.add(upgrade)

    def draw(self, screen):
        self.upgrade_block.draw(screen)
