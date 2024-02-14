import pygame
import math
from time import time

HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, obstacles, bullet_color):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill(bullet_color)
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 1
        self.angle = angle
        self.move_x = math.cos(self.angle)
        self.move_y = math.sin(self.angle)
        self.max_hits = 10
        self.hits = 0
        self.colision_initial_time = time()
        self.colision_final_time = time()
        self.bateu = False


    def update(self):
        self.colision_final_time = time()

        self.handle_move_x()
        self.handle_move_y()
        if not self.rect.colliderect(pygame.Rect(0, 0, 1280, 720)) or self.hits >= 6:
            self.kill()


    def handle_move_x(self):
        self.rect.x += self.speed * self.move_x

    def handle_move_y(self):
        self.rect.y += self.speed * self.move_y
    def handle_colision(self, direction):
        if direction == 'horizontal':
            self.colision_initial_time = time()
            self.move_x *= -1
            self.hits += 1
            self.bateu = True
            self.rect.x += self.speed * self.move_x

        if direction == 'vertical':
            if self.colision_final_time - self.colision_initial_time < 0.01:
                self.colision_initial_time = time()
                self.move_x *= -1
                self.hits -= 1
            self.move_y *= -1
            self.colision_initial_time = time()
            self.bateu = False
            self.hits += 1
            self.rect.y += self.speed * self.move_y
