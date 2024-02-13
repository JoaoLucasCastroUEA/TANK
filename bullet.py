import pygame
import math
from time import time

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, obstacles,bullet_color):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill(bullet_color)  # Fill the surface with black
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 1.5
        self.angle = angle  # Keep the angle in radians
        self.obstacles = obstacles
        self.move_x = math.cos(self.angle)
        self.move_y = math.sin(self.angle)
        self.max_hits = 10
        self.hits = 0

        self.colision_initial_time = time()
        self.colision_final_time = time()
        self.time_to_live_initial = time()
        self.time_to_live_final = time()
        self.time_to_live = 2.5


    def update(self):
        self.colision_final_time = time()
        self.time_to_live_final = time()

        self.rect.x += self.speed * self.move_x
        self.collision('horizontal')
        self.rect.y += self.speed * self.move_y
        self.collision('vertical')

        if not self.rect.colliderect(pygame.Rect(0, 0, 1280, 720)):
            self.kill()
        if self.time_to_live_final - self.time_to_live_initial > self.time_to_live:
            self.kill()

    def collision(self, direction):
        if direction == 'horizontal':
            for wall in self.obstacles:
                if self.colision_final_time - self.colision_initial_time > 0.01:
                    if self.rect.colliderect(wall):
                        self.move_x *= -1
                        self.colision_initial_time = time()
                        self.hits += 1


        if direction == 'vertical':
            for wall in self.obstacles:
                if self.colision_final_time - self.colision_initial_time > 0.01:
                    if self.rect.colliderect(wall):
                        self.move_y *= -1
                        self.colision_initial_time = time()
                        self.hits += 1