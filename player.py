import pygame
from gun import Gun

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Cria uma instância da classe Gun
        self.gun = Gun(self)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # Chama o método draw da instância de Gun
        self.gun.draw(self.screen)

    def take_commands(self):
        keys = pygame.key.get_pressed()

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

        # Chama o método update da instância de Gun
        self.gun.update()
