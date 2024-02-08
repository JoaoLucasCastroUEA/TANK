import pygame
import math

class Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player
        self.orbit_radius = 70
        self.orbit_height = -30
        self.orbit_speed = 0.02
        self.rotation_speed = 5

        self.original_image = pygame.Surface((12, 12))
        self.original_image.fill((255, 0, 0))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()

        self.angle = 0

    def update(self):
        self.angle += self.orbit_speed
        self.angle %= 2 * math.pi

        self.rect.x = self.player.rect.x + self.orbit_radius * math.cos(self.angle) + 20
        self.rect.y = self.player.rect.y + self.orbit_radius * math.sin(self.angle) + self.orbit_height + 50

        mouse_pos = pygame.mouse.get_pos()
        look_direction = pygame.math.Vector2(mouse_pos[0] - self.player.rect.centerx,
                                             mouse_pos[1] - self.player.rect.centery)

        if not look_direction.length_squared() == 0:
            look_direction.normalize()

            angle = math.degrees(math.atan2(look_direction.y, look_direction.x))

            if look_direction.x < 0:
                angle = 360 + angle  # Adiciona 360 para garantir que o ângulo seja positivo

            self.angle = math.radians(angle)

            # Cria uma nova imagem rotacionada
            self.image = pygame.transform.rotate(self.original_image, -angle + 90)
            print(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
