import pygame

from pygame.sprite import Sprite


class Ammo(Sprite):
    """Klasa definiujaca amunicje."""

    def __init__(self, main):
        """Inicializacja atrybutow pocisku."""
        super().__init__()
        self.screen = main.screen
        self.ship = main.ship
        self.settings = main.settings

        # Umieszczenie pocisku w lewym, gornym rogu ekranu.
        self.rect_pos = (0, 0)

        # Wymiary pocisku.
        self.rect_dimensions = (3, 15)

        # Utworzenie pocisku.
        self.rect = pygame.Rect(self.rect_pos, self.rect_dimensions)

        # Kolor pocisku.
        self.ammo_color = (0, 255, 255)

        # Umieszczenie pocisku na srodku gornej krawedzi statku.
        self.rect.midtop = self.ship.rect.midtop

        # Przechowywanie pozycji pocisku w wartosci zmiennoprzecinkowej.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_rect(self):
        """Wyrysowuje pocisk."""
        pygame.draw.rect(self.screen, self.ammo_color, self.rect)

    def update(self):
        """Aktualizacja pocisku na ekranie."""
        self.y -= self.settings.ammo_speed
        self.rect.y = self.y
