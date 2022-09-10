import pygame

import pygame.font

import os.path

from pygame.sprite import Sprite


class Button(Sprite):
    """Klasa definujaca przyciski w menu gry."""
    def __init__(self, main, text='', pos_x=50, pos_y=500):
        """Inicializacja atrybutow."""
        super().__init__()
        self.main = main
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen_rect.size
        self.settings = main.settings

        # Zaladowanie czcionki.
        self.font = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'), 92)

        # Kolor czcionki.
        self.font_color = (255, 255, 255)

        # Obiekt 'rect' przechowujacy wygenerowany obraz czcionki.
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 300, 70)

        # Pozycja startowa przyciskow.
        self.rect.x = -self.rect.width

        # Przechowywanie polozenia przyciskow w wartosci zmiennoprzecinkowej.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Wygenerowanie obiektu czcionki.
        self.font_image = self.font.render(self.text, False, self.font_color)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.center = self.rect.center

    def draw_rect(self):
        """Wyrysowuje na ekranie gotowy przycisk."""
        pygame.draw.rect(self.screen, self.font_color, self.rect, 5)
        self.screen.blit(self.font_image, self.font_rect)

    def update(self):
        """Uaktualnia polozenie przyciskow."""
        if self.settings.draw_menu_buttons:
            if self.rect.x < self.pos_x:
                self.font_rect.center = self.rect.center
                self.x += 1
                self.rect.x = self.x

    def blit_menu_buttons_again(self):
        """Ustala polozenie poczatkowe dla przyciskow menu."""
        self.rect.x = -self.rect.width
        self.x = float(self.rect.x)
        self.font_rect.center = self.rect.center
