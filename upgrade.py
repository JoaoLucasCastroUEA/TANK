import pygame

pygame.init()


class Upgrade(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.BLOCK_SIZE = 30
        self.color = color
        self.image = pygame.Surface((self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x * self.BLOCK_SIZE, y * self.BLOCK_SIZE))
