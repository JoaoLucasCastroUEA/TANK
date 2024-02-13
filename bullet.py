import pygame
import math
from time import time

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, obstacles):
        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))  # Fill the surface with black
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 2
        self.angle = angle  # Keep the angle in radians
        self.obstacles = obstacles
        self.move_x = math.cos(self.angle)
        self.move_y = math.sin(self.angle)
        self.max_hits = 10
        self.hits = 0

        self.colision_initial_time = time()
        self.colision_final_time = time()
        self.permision_colision = time()


    def update(self):

        self.colision_final_time = time()

        self.rect.x += self.speed * self.move_x
        self.collision('horizontal')
        self.rect.y += self.speed * self.move_y
        self.collision('vertical')


        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.kill()
        if self.hits > self.max_hits:
            self.kill()



    def collision(self, direction):
        if direction == 'horizontal':
            for wall in self.obstacles:
                if self.colision_final_time - self.colision_initial_time > 0.0001:

                    if self.rect.colliderect(wall):
                        if self.move_x > 0:
                            self.move_x *= -1
                            self.colision_initial_time = time()


                        else:
                            self.move_x *= -1
                            self.colision_initial_time = time()

                        self.hits += 1


        if direction == 'vertical':
            for wall in self.obstacles:
                if self.colision_final_time - self.colision_initial_time > 0.00001:
                    if self.rect.colliderect(wall):

                        if self.move_y > 0:
                            self.move_y *= -1
                            self.colision_initial_time = time()


                        else:
                            self.move_y *= -1
                            self.colision_initial_time = time()

                        self.hits += 1
