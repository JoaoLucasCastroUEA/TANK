import pygame
import math
from time import time
import os
from sound_manager import Sound_Manager

current_path = os.path.dirname(__file__)
sprite_path = os.path.join(current_path, 'Sprites')
bullet_img_path = os.path.join(sprite_path, 'img_bullet.png')


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, obstacles, bullet_color):
        super().__init__()

        self.sound_manager = Sound_Manager()
        self.image = pygame.image.load(bullet_img_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 1.6
        self.angle = angle
        self.move_x = math.cos(self.angle)
        self.move_y = math.sin(self.angle)
        self.max_hits = 10
        self.hits = 0

        self.initial_time = time()
        self.final_time = time()

    def update(self):
        self.final_time = time()
        self.handle_move_x()
        self.handle_move_y()
        if not self.rect.colliderect(pygame.Rect(0, 0, 1280, 720)) or self.hits >= self.max_hits:
            self.kill()

    def handle_move_x(self):
        self.rect.x += self.speed * self.move_x

    def handle_move_y(self):
        self.rect.y += self.speed * self.move_y

    def handle_collision(self, direction):
        if direction == 'horizontal':
            self.move_x *= -1
            self.hits += 1
            self.rect.x += self.speed * self.move_x
        if direction == 'vertical':
            if self.final_time - self.initial_time > 0.01:
                self.move_x *= -1
            self.move_y *= -1
            self.hits += 1
            self.rect.y += self.speed * self.move_y
