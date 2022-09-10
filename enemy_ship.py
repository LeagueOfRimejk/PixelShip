import pygame

import os.path

import random

from pygame.sprite import Sprite


class Enemy(Sprite):
    """Klasa definiujaca przeciwnikow."""

    def __init__(self, main):
        """Inicializacja atrybutow."""
        super().__init__()
        # Atrybuty klasy main.
        self.main = main
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings
        self.enemy_health = self.settings.enemy_health

        # Sciezka do obrazu statku przeciwnika.
        ship_path = 'resources/images/enemy_ship'

        # Zaladowanie obrazu statku przeciwnika.
        self.enemy = pygame.image.load(os.path.join(
            ship_path, 'enemy_ship.png')).convert_alpha()

        # Skalowanie obrazu i utworzenie jego 'rect'.
        self.enemy = pygame.transform.scale(self.enemy, (40, 80))
        self.rect = self.enemy.get_rect()

        # Zlokalizowanie wstepne przeciwnika na ekranie.
        self.rect.y = -self.rect.height
        self.rect.x = self.get_random_number(self.rect.width,
                                             self.screen_rect.width -
                                             self.rect.width)

        # Przechowywanie dokladnej pozycji statku przeciwnika
        # w postaci wartosci zmiennoprzecinkowej.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.health_rect_dimensions = (self.enemy_health / 2, 5)
        self.health_rect = pygame.Rect((0, 0), self.health_rect_dimensions)

    def get_random_number(self, start, end):
        """Losowa liczba."""
        random_number = random.randint(start, end)
        return random_number

    def update_enemy(self):
        """Aktualizacja polozenia statku."""
        self.y += self.settings.enemy_moving_speed

        # Zaktualizowanie polozenia statku.
        self.rect.y = self.y

        self.health_rect.midbottom = self.rect.midtop
        self.health_rect.y = self.y - self.health_rect.height * 2

    def blit_enemy(self):
        """Wyswietla statek na ekranie."""
        self.screen.blit(self.enemy, self.rect)

    def draw_enemy_health(self):
        pygame.draw.rect(self.screen, self.settings.health_bar_color, self.health_rect)

    def update_enemy_health(self):
        self.health_rect_dimensions = (self.enemy_health / 2, 5)
        self.health_rect = pygame.Rect((0, 0), self.health_rect_dimensions)
