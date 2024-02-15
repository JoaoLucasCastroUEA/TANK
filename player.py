import pygame
from gun import Gun
from time import time

class Player:
    def __init__(self, screen, obstacles, joystic, color, player_id):
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

        self.joystick = joystic
        self.joystick.init()

        # Cria uma instância da classe Gun
        self.gun = Gun(self,self.obstacles, self.joystick,self.bullet_color)
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
            self.gun.fire_bullet()
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


        self.analaog_x = self.joystick.get_axis(0)
        self.dx = self.analaog_x
        self.rect.x += self.dx * self.player_speed
        self.wall_collisions('horizontal')

        self.analaog_y = self.joystick.get_axis(1)
        self.dy = self.analaog_y
        self.rect.y += self.dy * self.player_speed
        self.wall_collisions('vertical')

        self.upgrade_collision(upgradeID,upgrades)


        # Normalizar o vetor de movimento na diagonal
        if self.dx != 0 and self.dy != 0:
            self.dx /= 1.414  # Aproximadamente 1.414 é a raiz quadrada de 2
            self.dy /= 1.414


        if self.joystick.get_axis(5) > -1:
            self.shoot()

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
            self.gun.update()

            # Chama o método draw da instância de Gun
            self.gun.draw(self.screen)
            self.fire_rate_final_time = time()

