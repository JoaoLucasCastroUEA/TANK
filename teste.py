import pygame
import math

pygame.init()

pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle detectado.")
    pygame.quit()
    quit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ângulo do Analógico")

def get_angle(x, y):
    """Calcula o ângulo a partir das coordenadas x e y."""
    angle = math.degrees(math.atan2(y, x))
    return angle if angle >= 0 else 360 + angle  # Garante que o ângulo é positivo

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    analog_x = joystick.get_axis(0)
    analog_y = joystick.get_axis(1)

    angle = get_angle(analog_x, analog_y)

    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Ângulo: {angle:.2f} graus", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
