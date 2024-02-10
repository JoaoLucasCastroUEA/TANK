import pygame
from gun import Gun
from time import time

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Cria uma instância da classe Gun
        self.gun = Gun(self)
        self.fire_rate = 0.1
        self.fire_rate_initial_time = time()
        self.fire_rate_final_time = time()

    def shoot(self):
        
        pass

    def player_commands(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1

        # Normalizar o vetor de movimento na diagonal
        if dx != 0 and dy != 0:
            dx /= 1.414  # Aproximadamente 1.414 é a raiz quadrada de 2
            dy /= 1.414

        self.rect.x += dx
        self.rect.y += dy

        if mouse[0]:
            if self.fire_rate_final_time - self.fire_rate_initial_time > self.fire_rate:
                self.gun.fire_bullet()
                self.fire_rate_initial_time = time()
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # Chama o método update da instância de Gun
        self.gun.update()

        # Chama o método draw da instância de Gun
        self.gun.draw(self.screen)
        self.fire_rate_final_time = time()
        print(self.fire_rate_final_time - self.fire_rate_initial_time)