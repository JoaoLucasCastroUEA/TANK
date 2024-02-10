import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))  # Fill the surface with black
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 2
        self.angle = angle  # Keep the angle in radians



    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        print(self.rect.x,self.rect.y)
        print(math.sin(self.angle))

        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.kill()

