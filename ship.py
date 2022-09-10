import pygame

import os.path


class Ship:
    """Klasa definiujaca statek kosmiczny."""

    def __init__(self, main):
        """Inicializacja atrybutow statku."""
        # Egzemplarze klasy glownej.
        self.main = main
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = main.settings
        self.health = main.settings.ship_health

        # Zaladowanie obrazu statku i utworzenie jego 'rect'.
        image_path = 'resources/images/ship/'

        self.ship = pygame.image.load(os.path.join(image_path, 'new_ship.png')).convert_alpha()
        self.ship = pygame.transform.scale(self.ship, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.ship.get_rect()

        # Ustalenie pozycji statku na srodku dolnej krawedzi ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        # Przechowywanie pozycji statku w wartosci zmiennoprzecinkowej.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Stan poruszania sie statku.
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.health_rect_dimensions = (self.health / 2, 5)
        self.health_rect = pygame.Rect((0, 0), self.health_rect_dimensions)

    def update_ship(self):
        """Aktualizuje polozenie statku."""
        if self.moving_up and self.rect.top > (self.screen_rect.height - 300):
            self.y -= self.settings.ship_moving_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height - self.health_rect.height * 2:
            self.y += self.settings.ship_moving_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_moving_speed
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.x += self.settings.ship_moving_speed

        # Aktualizacja polozenia statku.
        self.rect.x = self.x
        self.rect.y = self.y - self.health_rect.height * 2

        self.health_rect.midtop = self.rect.midbottom
        self.health_rect.y = self.rect.bottom + self.health_rect.height

    def blit_ship(self):
        """Wyrysowuje statek na ekranie."""
        self.screen.blit(self.ship, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
        self.y = self.rect.y

    def draw_health(self):
        pygame.draw.rect(
            self.screen, self.settings.health_bar_color, self.health_rect
        )

    def update_health(self):
        self.health_rect_dimensions = (self.health / 2, 5)
        self.health_rect = pygame.Rect((0, 0), self.health_rect_dimensions)

    def health_level_up(self):
        self.health = self.main.settings.ship_health
