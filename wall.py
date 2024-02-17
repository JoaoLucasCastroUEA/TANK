import pygame
import os

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.BLOCK_SIZE = 40
        # Corrige o caminho para a imagem da parede
        self.image = pygame.image.load(os.path.join("Sprites", "img_wall.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.rect = self.image.get_rect(topleft=(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE))
