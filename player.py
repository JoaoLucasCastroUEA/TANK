import pygame
from gun import Gun
from time import time

class Player:
    def __init__(self, screen, obstacles, color, player_id):
        #def __init__(self, screen, obstacles, joystic, color, player_id):

        self.screen = screen
        self.width = 35
        self.height = 35
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(100, 200, self.width, self.height)
        self.obstacles = obstacles
        self.dx = 0
        self.dy = 0

        self.player_id = player_id
        self.bullet_color = color
        self.player_life = 10
        self.player_speed = 1


        # Cria uma instância da classe Gun
        self.fire_rate = 0.5
        self.fire_rate_initial_time = time()
        self.fire_rate_final_time = time()

        # Upgrade manager
        self.upgrade_timer = 5
        self.upgrade_initial_timer = time()
        self.upgrade_final_timer = time()
        self.has_upgrade = False

        # é hora de trollar
        if pygame.joystick.get_count() == 0:
            print("Nenhum controle detectado.")



    def shoot(self):
        if self.fire_rate_final_time - self.fire_rate_initial_time > self.fire_rate:
            self.fire_rate_initial_time = time()

    def Upgrade(self,upgradeID, upgrades):

        if self.has_upgrade:
            self.upgrade_final_timer = time()
            if self.upgrade_final_timer - self.upgrade_initial_timer > self.upgrade_timer:
                self.upgrade_manager('END')
                self.upgrade_initial_timer = time()
                self.has_upgrade = False
        self.dx = 0
        self.dy = 0

        self.upgrade_collision(upgradeID,upgrades)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.dy = -1
        if keys[pygame.K_s]:
            self.dy = 1

        if keys[pygame.K_d]:
            self.dx = 1
        if keys[pygame.K_a]:
            self.dx = -1

        self.rect.x += self.player_speed * self.dx
        self.wall_collisions('horizontal')

        self.rect.y += self.player_speed * self.dy
        self.wall_collisions('vertical')


        # Normalizar o vetor de movimento na diagonal
        if self.dx != 0 and self.dy != 0:
            self.dx /= 1.414  # Aproximadamente 1.414 é a raiz quadrada de 2
            self.dy /= 1.414



    def wall_collisions(self, direction):
        if direction == 'horizontal':
            for wall in self.obstacles:
                if self.rect.colliderect(wall):
                    if self.dx > 0:
                        self.rect.right = wall.rect.left

                    if self.dx < 0:
                        self.rect.left = wall.rect.right

        if direction == 'vertical':
            for wall in self.obstacles:
                if self.rect.colliderect(wall):
                    if self.dy > 0:
                        self.rect.bottom = wall.rect.top

                    if self.dy < 0:
                        self.rect.top = wall.rect.bottom

    def upgrade_collision(self,upgrade_ID,upgrades):
        for upgrade in upgrades:
            if self.rect.colliderect(upgrade):
                self.upgrade_manager(upgrade_ID.upgrade_ID)
                upgrade.kill()

    def upgrade_manager(self, upgradeID):
        if upgradeID == 'END':
            self.fire_rate = 0.5
            self.player_speed = 1
            self.has_upgrade = False

        if upgradeID == 'fire rate':
            self.fire_rate = 0.1
            self.has_upgrade = True

        if upgradeID == 'speed':
            self.player_speed = 2
            self.has_upgrade = True




    def draw(self):
        if self.player_life > 0:
            pygame.draw.rect(self.screen, self.color, self.rect)
            # Chama o método update da instância de Gun

            # Chama o método draw da instância de Gun
            self.fire_rate_final_time = time()

