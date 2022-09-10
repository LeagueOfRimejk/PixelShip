import pygame

import pygame.font

import os.path


class GameLogo:
    """Klasa glowna definiujaca logo gry."""

    def __init__(self, main):
        """Inicializacja atrybutow."""
        self.screen = main.screen
        self.settings = main.settings
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen_rect.size

        # Zaladowanie obrazu ziemi i statku.
        earth_image = 'resources/images/background'
        ship_image = 'resources/images/ship'

        # Ustalenie wymiarow i parametrow statku oraz utworzenie jego 'rect'.
        self.ship = pygame.image.load(os.path.join(ship_image, 'new_ship.png')).convert_alpha()
        self.ship = pygame.transform.scale(self.ship, (50, 100))
        self.ship = pygame.transform.rotate(self.ship, 40)
        self.ship_rect = self.ship.get_rect()

        # Ustalenie wymiarow i parametrow Ziemi oraz utworzenie jej 'rect'.
        self.earth = pygame.image.load(os.path.join(earth_image, 'earth.png')).convert_alpha()
        self.earth = pygame.transform.scale(self.earth, (175, 175))
        self.earth_rect = self.earth.get_rect()

        # Zdefiniowanie pozycji startowej Ziemi.
        self.earth_rect.x = 150
        self.earth_rect.y = -self.earth_rect.height

        # Dokladne przechowywanie polozenia Ziemi w wartosci
        # zmiennoprzecinkowej.
        self.earth_x = float(self.earth_rect.x)
        self.earth_y = float(self.earth_rect.y)

        # Zdefiniowanie pozycji startowej statku.
        self.ship_rect.x = self.earth_rect.x + 70
        self.ship_rect.y = -self.ship_rect.height

        # Dokladne przechowywanie polozenia statku w wartosci
        # zmiennoprzecinkowej.
        self.ship_x = float(self.ship_rect.x)
        self.ship_y = float(self.ship_rect.y)

        # Zaladowanie stylu czcionki dla napisu gry.
        font_path = 'resources/fonts/pixel_font2'
        self.font = pygame.font.Font(os.path.join(font_path, 'title_font.ttf'), 102)

        # Kolor czcionki.
        self.font_color = (255, 255, 255)

        # Utworzenie 'rect' dla napisu z nazwa gry.
        self.font_rect = pygame.Rect(0, 0, 500, 100)

        # Dokladne polozenie obiektu font_rect w wartosci zmiennoprzecinkowej.
        self.font_x = float(self.font_rect.x)
        self.font_y = float(self.font_rect.y)

        # Wyrenderowanie obrazu z tytulem gry.
        self.font_image = self.font.render('Pixel Ship', False, self.font_color)
        self.font_image_rect = self.font_image.get_rect()

    def update_logo(self):
        """Aktualizuje polozenie loga gry."""
        if self.earth_rect.y < self.earth_rect.height / 3:

            # Ziemia.
            self.earth_y += self.settings.logo_falling_speed
            self.earth_rect.y = self.earth_y

            # Obiekt 'rect' napisu gry.
            self.font_rect.left = self.earth_rect.bottom
            self.font_y += self.settings.logo_falling_speed
            self.font_rect.y = self.font_y

            # Obraz napisu gry.
            self.font_image_rect.x = self.font_x
            self.font_image_rect.y = self.font_y
            self.font_image_rect.center = self.font_rect.center

            # Statek.
            self.ship_y += self.settings.logo_falling_speed
            self.ship_rect.y = self.ship_y + 30
        else:
            # Warunek odpowiadajacy za wyrysowanie przyciskow menu.
            self.settings.draw_menu_buttons = True

    def blit_logo(self):
        """Wyrysowuje logo na ekranie glownym."""
        pygame.draw.rect(self.screen, (255, 255, 255), self.font_rect, -1)

        self.screen.blit(self.font_image, self.font_image_rect)
        self.screen.blit(self.earth, self.earth_rect)
        self.screen.blit(self.ship, self.ship_rect)

    def blit_logo_again(self):
        """Ustala wartosci poczatkowe polozenia loga."""
        # Ziemia.
        self.earth_rect.y = -self.earth_rect.height
        self.earth_y = float(self.earth_rect.y)

        # Statek.
        self.ship_rect.y = -self.ship_rect.height
        self.ship_y = float(self.ship_rect.y)

        # Napis Gry.
        self.font_rect.y = self.earth_rect.bottom
        self.font_y = float(self.font_rect.y)

        # Warunek odpowiadajacy za wyrysowanie przyciskow menu.
        self.settings.draw_menu_buttons = False
