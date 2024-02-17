import pygame
import os

class Credits:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.bg_image = pygame.image.load(os.path.join("Sprites", "img_bg_credits.png")).convert()
        self.return_button = pygame.image.load(os.path.join("Sprites", "img_return_credits.png")).convert_alpha()

        # Members information
        self.members_info = [
            ("Coordinator", "Profº Jucimar Maia da Silva"),
            ("", ""),
            ("Team", "- João Lucas Noronha"),
            ("", "- Juliana Ballin Lima"),
            ("", "- Renato Barbosa")
        ]

        # Text settings
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.line_spacing = 40
        self.text_position = (self.width // 2, 300)

    def show_credits(self):
        running = True
        while running:
            self.screen.blit(self.bg_image, (0, 0))
            
            # Draw members' credits
            for i, (title, name) in enumerate(self.members_info):
                text = self.font.render(f"{title}", True, self.text_color)
                text_rect = text.get_rect(center=(self.width // 2, self.text_position[1] + i * self.line_spacing))
                self.screen.blit(text, text_rect)

                text = self.font.render(name, True, self.text_color)
                text_rect = text.get_rect(center=(self.width // 2, text_rect.bottom + 20))
                self.screen.blit(text, text_rect)

            # Draw return button
            return_button_rect = self.return_button.get_rect(center=(self.width // 2, 600))
            self.screen.blit(self.return_button, return_button_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if return_button_rect.collidepoint(mouse_pos):
                        running = False
