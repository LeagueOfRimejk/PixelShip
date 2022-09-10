import pygame

import os.path


class Sounds:
    def __init__(self, main):
        pygame.mixer.init()
        self.main = main
        self.settings = main.settings

        self.shot_sound = 'resources/sounds/'
        self.laser = pygame.mixer.Sound(os.path.join(self.shot_sound, 'laser.wav'))
        self.laser.set_volume(0.2)

        self.enemy_laser = pygame.mixer.Sound(os.path.join(self.shot_sound, 'laser_enemy.wav'))
        self.enemy_laser.set_volume(0.4)

        self.player_crash = pygame.mixer.Sound(os.path.join(self.shot_sound, 'player_crash.wav'))
        self.player_crash.set_volume(0.7)

        self.enemy_crash = pygame.mixer.Sound(os.path.join(self.shot_sound, 'enemy_crash.wav'))
        self.enemy_crash.set_volume(0.4)

        self.playlist = self.shot_sound
        self.playlist += f'playlist/'

        self.getting_hit = pygame.mixer.Sound(os.path.join(self.shot_sound, 'hit.wav'))
        self.getting_hit.set_volume(1.0)

    def laser_sound(self):
        pygame.mixer.Sound.play(self.laser)

    def enemy_laser_sound(self):
        pygame.mixer.Sound.play(self.enemy_laser)

    def player_crash_sound(self):
        pygame.mixer.Sound.play(self.player_crash)

    def enemy_crash_sound(self):
        pygame.mixer.Sound.play(self.enemy_crash)

    def get_hit_sound(self):
        pygame.mixer.Sound.play(self.getting_hit)

    def main_menu_sound(self):
        pygame.mixer.music.load(os.path.join(self.playlist, 'zabutom2.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def in_game_sound(self):
        pygame.mixer.music.load(os.path.join(self.playlist, 'zabutom.mp3'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0, 1500)

    def stop_play_list(self):
        pygame.mixer.music.stop()
