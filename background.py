import pygame
import pygame.gfxdraw

from pygame.sprite import Sprite

import random


class Background(Sprite):
    """Klasa przechowujaca parametry tla."""
    def __init__(self, main):
        """Inicializacja atrybutow tla."""
        # Ekran, rect, wymiary.
        super().__init__()
        # Utworzenie egzemplarza ekranu gry.
        self.main = main
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen_rect.size

        # Parametry kol.
        self.how_many_circles = self.get_random_number(1, 20)
        self.how_many_bounces = self.get_random_number(5, 25)
        self.bounce = True
        self.bounce_count = 0
        self.circle_speed = 2.7

        # Kierunek poruszania sie kol.
        self.circle_direction_y = 1
        self.circle_direction_x = 1

        # Ustalenie kierunku poruszania sie kol.
        self.set_spawn_direction()

        # Promien kola.
        self.circle_radius = 30

        # Losowa pozycja kol na ekranie.
        self.circle_x = random.randint(self.circle_radius, self.screen_height - self.circle_radius)
        self.circle_y = random.randint(self.circle_radius, self.screen_height - self.circle_radius)

        # Dokladna pozycja kola w postaci zmiennoprzecinkowej.
        self.x = float(self.circle_x)
        self.y = float(self.circle_y)

        # Dostepne kolory kol.
        self.yellow = (255, 255, 25)
        self.caribbean_green = (0, 204, 136)
        self.red = (227, 38, 54)
        self.light_blue = (77, 225, 255)
        self.orange = (255, 126, 0)
        self.purple = (255, 128, 255)
        self.pale_blue = (201, 255, 229)
        self.neon_green = (51, 255, 51)
        self.peach = (255, 230, 179)

        # Losowy kolor kola.
        self.random_color = self.get_circle_random_colors()

    def get_random_number(self, start, end):
        """Generuje losowa liczbe."""
        random_number = random.randint(start, end)
        return random_number

    def get_circle_random_colors(self):
        """Wybiera losowy kolor dla kola."""
        random_color = random.randint(1, 9)
        if random_color == 1:
            return self.yellow
        if random_color == 2:
            return self.caribbean_green
        if random_color == 3:
            return self.red
        if random_color == 4:
            return self.light_blue
        if random_color == 5:
            return self.orange
        if random_color == 6:
            return self.purple
        if random_color == 7:
            return self.pale_blue
        if random_color == 8:
            return self.neon_green
        if random_color == 9:
            return self.peach

    def draw_circle(self):
        """Wyrosowuje kolo na ekranie."""
        pygame.gfxdraw.aacircle(self.screen, int(self.circle_x), int(self.circle_y), self.circle_radius,
                                self.random_color)
        pygame.gfxdraw.filled_circle(self.screen, int(self.x), int(self.y), self.circle_radius, self.random_color)

    def spawn_circle_again(self):
        """Tworzy ponownie kolo na ekranie."""
        self.set_spawn_direction()
        self.circle_x = random.randint(self.circle_radius, self.screen_height - self.circle_radius)
        self.circle_y = random.randint(self.circle_radius, self.screen_height - self.circle_radius)

    def update(self):
        """Aktualizacja polozenia kola."""
        if self.circle_direction_y == 1:
            self.y += self.circle_speed * self.circle_direction_y
            self.x += self.circle_speed * self.circle_direction_x

        if self.circle_direction_y == -1:
            self.y += self.circle_speed * self.circle_direction_y
            self.x += self.circle_speed * self.circle_direction_x

        # Zaktualizowanie polozenia kola.
        self.circle_y = self.y
        self.circle_x = self.x

    def set_spawn_direction(self):
        """Ustala kierunek poruszania sie kola po jego wyrysowaniu."""
        condition = random.randint(0, 1)
        if condition == 0:
            self.circle_direction_y = 1
            self.circle_direction_x = 1
        else:
            self.circle_direction_y = -1
            self.circle_direction_x = -1

    def change_circle_direction(self):
        """Zmienia kierunek kola."""
        if self.bounce_count >= self.how_many_bounces:
            self.bounce = False

        if self.bounce:
            if self.circle_y > self.screen_height - self.circle_radius:
                self.circle_direction_y *= -1
                self.bounce_count += 1

            if self.circle_y < self.circle_radius:
                self.circle_direction_y *= -1
                self.bounce_count += 1

            if self.circle_x > self.screen_width - self.circle_radius:
                self.circle_direction_x *= -1
                self.bounce_count += 1

            if self.circle_x < self.circle_radius:
                self.circle_direction_x *= -1
                self.bounce_count += 1
