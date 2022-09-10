import pygame

from pygame.sprite import Sprite


class EnemyAmmo(Sprite):
    """Klasa definiujaca amunicje."""

    def __init__(self, main):
        """Inicializacja atrybutow pocisku."""
        super().__init__()
        self.screen = main.screen
        self.settings = main.settings
        self.enemy = main.enemy

        # Umieszczenie pocisku w lewym, gornym rogu ekranu.
        self.rect_pos = (0, 0)

        # Wymiary pocisku.
        self.rect_dimensions = (3, 15)

        # Utworzenie pocisku.
        self.rect = pygame.Rect(self.rect_pos, self.rect_dimensions)

        # Kolor pocisku.
        self.ammo_color = (255, 20, 15)

        # Umieszczenie pocisku na srodku dolnej krawedzi statku.
        for enemy in self.enemy:
            self.rect.midbottom = enemy.rect.midbottom

        # Przechowywanie pozycji pocisku w wartosci zmiennoprzecinkowej.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_ammo(self):
        """Wyrysowuje pocisk."""
        pygame.draw.rect(self.screen, self.ammo_color, self.rect)

    def update_ammo(self):
        """Aktualizacja pocisku na ekranie."""
        self.y += self.settings.ammo_speed
        self.rect.y = self.y
