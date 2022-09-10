import pygame

import pygame.font

import os.path

from button import Button


class ShipDevelopmentMenu(Button):

    def __init__(self, main, text='', pos_x=50, pos_y=500):
        super().__init__(main, text, pos_x, pos_y)
        self.main = main

        # Zaladowanie czcionki.
        self.font = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'), 52)

        # Polozenie startowe nowych przyciskow.
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 350, 70)

        # Lokalizacja obrazu tekstu na przycisku.
        self.font_image = self.font.render(self.text, False, self.font_color)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.center = self.rect.center

        # Utworzenie powierzchni z kanalem alpha.
        self.surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        self.surface = self.surface.convert_alpha()

        # Wyrysowanie tla dla menu rozwoju statku.
        self.rect2 = pygame.Rect(0, 0, 700, 500)
        self.rect2.center = self.screen.get_rect().center

        # Atrybuty potrzebne do ustalenia statystyk statku.
        self.ship_damage = main.settings.ship_damage
        self.ship_health = main.settings.ship_health
        self.ship_defence = main.settings.ship_defence
        self.ship_guns = main.settings.ship_guns
        self.shooting_frequency = main.settings.shooting_frequency

        self.stats_font = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'), 48)

    def create_surface_for_ship_dev(self):
        self.screen.blit(self.surface, self.surface.get_rect())
        pygame.draw.rect(self.surface, (128, 128, 128, 200), self.rect2)

    def create_ship_stats(self):
        self.rect = pygame.Rect(self.rect2.x + 10, self.rect2.y, 200, 40)

        self.ship_stats = {'Statystyki': 'statku', 'Atak': self.ship_damage, 'Obrona': self.ship_defence,
                           'Zycie': self.ship_health, 'Ilosc dzial': self.ship_guns,
                           'Szybkosc ataku': self.shooting_frequency / 500}

        for key, value in self.ship_stats.items():

            if key == 'Statystyki':
                self.text = f'{key} {str(value)}'
                self.stats_font = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'),
                                                   64)
            else:
                self.text = f'{key}: {str(value)}'
                self.stats_font = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'),
                                                   42)

            self.font_image = self.stats_font.render(self.text, False, self.font_color)
            self.font_rect = self.font_image.get_rect()
            self.font_rect.midleft = self.rect.midleft

            if key == 'Statystyki':
                pygame.draw.rect(self.screen, self.font_color, self.rect, -1)

                self.screen.blit(self.font_image, self.font_rect)

            else:

                pygame.draw.rect(self.screen, self.font_color, self.rect, -1)
                self.screen.blit(self.font_image, self.font_rect)

            self.rect.y += self.rect.height + 10

    def update_ship_stats(self):
        self.ship_damage = self.main.settings.ship_damage
        self.ship_health = self.main.settings.ship_health
        self.ship_defence = self.main.settings.ship_defence
        self.ship_guns = self.main.settings.ship_guns
        self.shooting_frequency = self.main.settings.shooting_frequency

    def update(self):
        """Aktualizuje polozenie przyciskow na srodku ekranu."""
        self.font_rect.center = self.rect.center
