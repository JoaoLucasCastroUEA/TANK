import pygame
pygame.init()

# Inicializa o joystick
pygame.joystick.init()

# Verifica se há pelo menos um joystick conectado
if pygame.joystick.get_count() > 0:
    # Obtém o primeiro joystick disponível
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Loop principal
    while True:
        # Obtém o estado de todos os botões do joystick
        buttons = joystick.get_button(1)

        # Exibe o estado de cada botão
        for i in range(len(buttons)):
            print(f'Botão {i}: {buttons[i]}')

        # Adicione aqui o resto do seu código ou lógica de jogo

# Finaliza o pygame
pygame.quit()
