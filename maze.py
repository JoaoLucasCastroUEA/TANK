import pygame
from wall import Wall

class Maze:
    def __init__(self, pattern, screen_width, screen_height):
        self.pattern = pattern

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.walls = pygame.sprite.Group()
        self.wall_width = screen_width // len(pattern[0])
        print(self.wall_width)
        self.wall_height = screen_height // len(pattern)
        print(self.wall_height)

        print(self.wall_width,self.wall_height)
        for y, row in enumerate(pattern):
            for x, char in enumerate(row):
                if char == "#":
                    wall = Wall(x * self.wall_width, y * self.wall_height, self.wall_width, self.wall_height)
                    self.walls.add(wall)

    def draw(self, screen):
        self.walls.draw(screen)
