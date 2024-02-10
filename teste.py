import pygame
import sys

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10

    def move(self):
        self.y -= 10

# Inicializar o Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Atirando com Pygame")

# Cores
black = (0, 0, 0)
white = (255, 255, 255)

# Jogador
class Player:
    def __init__(self):
        self.size = 50
        self.x = width // 2 - self.size // 2
        self.y = height - self.size - 10

player = Player()

# Projéteis
projectiles = []

# Loop principal
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse
            # Adicionar um novo projétil na posição do jogador
            projectiles.append(Bullet(player.x + player.size // 2, player.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < width - player.size:
        player.x += 5

    # Atualizar a posição dos projéteis
    for projectile in projectiles:
        projectile. move()

    # Filtrar projéteis que saíram da tela
    projectiles = [projectile for projectile in projectiles if projectile.y > 0]

    # Desenhar na tela
    screen.fill(black)
    pygame.draw.rect(screen, white, (player.x, player.y, player.size, player.size))

    for projectile in projectiles:
        pygame.draw.circle(screen, white, (projectile.x, projectile.y), projectile.size)

    pygame.display.flip()
    clock.tick(60)
