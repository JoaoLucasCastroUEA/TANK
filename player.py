import pygame
from gun import Gun
from time import time

class Player:
    def __init__(self, screen, obstacles, joystic):
        self.screen = screen
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(100, 200, self.width, self.height)
        self.obstacles = obstacles
        self.dx = 0
        self.dy = 0

        self.joystick = joystic
        self.joystick.init()

        # Cria uma instância da classe Gun
        self.gun = Gun(self,self.obstacles, self.joystick)
        self.fire_rate = 0.1
        self.fire_rate_initial_time = time()
        self.fire_rate_final_time = time()

        # é hora de trollar
        if pygame.joystick.get_count() == 0:
            print("Nenhum controle detectado.")



    def shoot(self):
        if self.fire_rate_final_time - self.fire_rate_initial_time > self.fire_rate:
            self.gun.fire_bullet()
            self.fire_rate_initial_time = time()

    def player_commands(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        self.dx = 0
        self.dy = 0

        # # bloco de andar no eixo x
        # if keys[pygame.K_a]:
        #     self.dx -= 1
        # if keys[pygame.K_d]:
        #     self.dx += 1
        # self.rect.x += self.dx
        #
        #
        # # bloco de andar no eixo y
        # if keys[pygame.K_w]:
        #     self.dy -= 1
        # if keys[pygame.K_s]:
        #     self.dy += 1
        # self.rect.y += self.dy


        self.analaog_x = self.joystick.get_axis(0)
        self.dx = self.analaog_x
        self.rect.x += self.dx
        self.collisions('horizontal')

        self.analaog_y = self.joystick.get_axis(1)
        self.dy = self.analaog_y
        self.rect.y += self.dy
        self.collisions('vertical')


        # Normalizar o vetor de movimento na diagonal
        if self.dx != 0 and self.dy != 0:
            self.dx /= 1.414  # Aproximadamente 1.414 é a raiz quadrada de 2
            self.dy /= 1.414


        if mouse[0]:
            self.shoot()
        if self.joystick.get_axis(5) > -1:
            self.shoot()

    def collisions(self, direction):
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
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # Chama o método update da instância de Gun
        self.gun.update()

        # Chama o método draw da instância de Gun
        self.gun.draw(self.screen)
        self.fire_rate_final_time = time()

