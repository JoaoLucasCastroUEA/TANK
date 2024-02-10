import pygame
import math
from bullet import Bullet

class Gun(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.player = player
        self.orbit_radius = 70
        self.orbit_height = -30
        self.orbit_speed = 0.02
        self.rotation_speed = 5

        # Load the image with transparency
        self.original_image = pygame.image.load(
            "C:\\Users\\joaoj\\OneDrive\\Documentos\\GitHub\\TANK\\Sprites\\Arma.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (24, 24))
        self.original_image.set_colorkey((255, 0, 255))  # Set the transparent color (use the color of your background)

        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()

        self.angle = 0
        self.bullet = Bullet(self.rect.x, self.rect.y, self.angle)
        self.bullets = pygame.sprite.Group()



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
                angle = 360 + angle

            self.angle = math.radians(angle)
            rotated_image = pygame.transform.rotate(self.original_image, -angle)
            self.image = rotated_image.convert_alpha()
        self.bullets.update()

    def fire_bullet(self):
        bullet = Bullet(self.rect.x, self.rect.y, self.angle)
        self.bullets.add(bullet)
        print(self.bullets)



    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullet.update()
        self.bullets.draw(screen)


