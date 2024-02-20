import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("Sprites/img_wall.png").convert()  # Carrega a imagem da parede
        self.rect = self.image.get_rect(topleft=(x, y))
