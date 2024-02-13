import pygame
from wall import Wall

pygame.init()


class Maze:
    def __init__(self, pattern):
        self.pattern = pattern
        self.color = (0,0,0)
        self.walls = pygame.sprite.Group()
        for y, row in enumerate(pattern):
            for x, char in enumerate(row):
                if char == "#":
                    wall = Wall(x, y, self.color)
                    self.walls.add(wall)

    def draw(self, screen):
        self.walls.draw(screen)
