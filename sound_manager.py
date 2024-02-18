import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()

class Sound_Manager:


    def game_music_loop(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=-1)

    game_music_file_path = 'Sounds/Music/gamemusic.wav'

    game_music_loop(game_music_file_path)

    def menu_music_loop(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(loops=-1)

    menumusic_file_path = 'Sounds/Music/menumusic.wav'

    menu_music_loop(menumusic_file_path)
