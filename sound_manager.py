import pygame
import random

pygame.init()
pygame.mixer.init()

class Sound_Manager:
    def __init__(self):
        self.music_file = 'Sounds/Music/gamemusic.wav'
        self.menu_music_file = 'Sounds/Music/menumusic.wav'
        self.hitsound_file = 'Sounds/Game/hit1.wav'

    def play_game_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.4)

    def play_menu_music(self):
        pygame.mixer.music.load(self.menu_music_file)
        pygame.mixer.music.play(loops=-1)

