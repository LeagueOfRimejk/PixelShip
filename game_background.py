import pygame

import random

from pygame.sprite import Sprite


class GameBackground(Sprite):
    """Klasa definiujaca przewijajace sie tlo gry."""

    def __init__(self, main):
        """Inicializacja atrybutow tla."""
        super().__init__()
        # Utworzenie egzemplarzy 'main'.
        self.main = main
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings

        # Utworzenie kwadratow symulujacych gwiazdy.
        self.star = pygame.Rect(0, 0, self.get_random_number(1, 3), self.get_random_number(1, 3))

        # Kolor gwiazdy.
        self.star_color = (255, 255, 255)

        # Umieszczenie gwiazdy w losowym polozeniu na osi X,
        # na osi Y rowniez losowo do momenty uzupelnienia
        # sie grupy 'main.stars', pozniej powyzej ekranu gry.

        # Os X
        self.star.x = self.get_random_number(self.star.width, self.screen_rect.width - self.star.width)

        # Os Y
        if len(self.main.stars) < self.settings.how_many_stars - 5:
            self.star.y = self.get_random_number(self.star.height, self.screen_rect.height - self.star.height)
            self.how_many_stars = self.settings.how_many_stars
        else:
            self.star.y = -self.star.height
            self.how_many_stars = self.get_random_number(1, 140)

        # Przechowywanie polozenia gwiazdy w wartosci zmiennoprzecinkowej.
        self.x = float(self.star.x)
        self.y = float(self.star.y)

    def get_random_number(self, start, end):
        """Generuje losowa liczbe z przedzialu."""
        random_number = random.randint(start, end)
        return random_number

    def draw_rect(self):
        """Wyrysowuje kwadrat."""
        pygame.draw.rect(self.screen, self.star_color, self.star)

    def update(self):
        """Uaktualnia pozycje kwadratu o wskazana wartosc w zmiennej."""
        self.y += self.settings.star_falling_speed

        # Aktualizacja pozycji gwiazdy.
        self.star.y = self.y
