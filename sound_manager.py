import pygame

pygame.init()
pygame.mixer.init()

class Sound_Manager:
    def __init__(self):
        self.music_file = 'Sounds/Music/gamemusic.wav'

    def play_game_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.4)