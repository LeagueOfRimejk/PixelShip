import pygame

import random

import os.path

from pygame.sprite import Sprite


class GameStats(Sprite):
    """Klasa definiujaca interface podczas gry."""

    def __init__(self, main):
        """Inicializacja atrybutow."""
        super().__init__()
        self.main = main
        self.screen = main.screen
        self.actual_level = main.settings.actual_level
        self.ship_damage = main.settings.ship_damage
        self.ship_defence = main.settings.ship_defence
        self.ship_guns = main.settings.ship_guns
        self.shooting_frequency = main.settings.shooting_frequency
        self.guns_count = main.settings.guns_count
        self.ammo_speed = main.settings.ammo_speed
        self.enemy_health = main.settings.enemy_health
        self.enemy_damage = main.settings.enemy_damage
        self.how_many_enemies = main.settings.how_many_enemies
        self.ship_health = main.ship.health
        self.available_life = main.settings.available_life
        self.how_many_enemies_left = main.settings.how_many_enemies_left
        self.star_falling_speed = main.settings.star_falling_speed
        self.settings = main.settings

        # Wczytanie obrazu statku potrzebnego do wyswietlenia liczby zyc.
        ship_image_path = 'resources/images/ship'
        self.ship_image = pygame.image.load(os.path.join(ship_image_path, 'new_ship.png')).convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, (30, 60))
        # Parametr 'rect' statku gracza.
        self.ship_rect = self.ship_image.get_rect()

        # Pozycja statku na ekranie.
        self.ship_rect.x = 10
        self.ship_rect.y = 10

        # Wczytanie obrazu krzyza zycia.
        health_cross_image = 'resources/images/health_cross'
        self.health_cross_image = pygame.image.load(
            os.path.join(health_cross_image, 'health_cross.png')).convert_alpha()
        self.health_cross_image = pygame.transform.scale(self.health_cross_image, (30, 40))
        # Parametr 'rect' krzyza.
        self.health_cross_rect = self.health_cross_image.get_rect()

        # Pozycja krzyza na ekranie.
        self.health_cross_rect.x = 10
        self.health_cross_rect.y = 10 * 2 + self.ship_rect.height

        # Wczytanie czcinki potrzebnej do wyswietlenia aktualnego poziomu zycia.
        self.font = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'), 72)
        self.font_color = (255, 10, 5)

        # Utworzenie obiektu 'rect' dla wyswietlenia aktualnego zycia.
        self.container_rect = pygame.Rect(30 + self.health_cross_rect.width, 10 + self.ship_rect.height, 50, 50)

        # Tekst do wyswietlenia.
        self.text = str(round(self.ship_health, 0))
        self.font_image = self.font.render(self.text, False, self.font_color)
        self.font_rect = self.font_image.get_rect()

        # Umieszczenie obrazu tekstu na srodku jego 'kontenera'.
        self.font_rect.center = self.container_rect.center

        # Wczytanie czcinki potrzebnej do wyswietlenia aktualnego poziomu zycia.
        self.font_2 = pygame.font.Font(os.path.join('resources/fonts/pixel_font/', 'advanced_pixel-7.ttf'), 72)

        # Utworzenie obiektu 'rect' dla wyswietlenia liczby pozostalych przeciwnikow.
        self.container_rect_2 = pygame.Rect(self.main.screen_width - 40, 10, 50, 50)
        self.container_rect_2.right = self.screen.get_rect().right - 10

        # Tekst do wyswietlenia.
        self.text_2 = str(self.how_many_enemies_left)
        self.font_image_2 = self.font_2.render(self.text_2, False, self.font_color)
        self.font_rect_2 = self.font_image_2.get_rect()

        # Umieszczenie obrazu tekstu na srodku jego 'kontenera'.
        self.font_rect_2.center = self.container_rect_2.center

        # Wczytanie obrazu statku przeciwnika.
        enemy_ship = 'resources/images/enemy_ship/'
        self.enemy_ship_image = pygame.image.load(os.path.join(enemy_ship, 'enemy_ship.png')).convert_alpha()
        self.enemy_ship_image = pygame.transform.scale(self.enemy_ship_image, (40, 75))
        self.enemy_ship_image = pygame.transform.rotate(self.enemy_ship_image, -140)

        # Utworzenie parametru 'rect' dla obrazu przeciwnika.
        self.enemy_ship_rect = self.enemy_ship_image.get_rect()

        # Zlokalizowanie na ekranie pozycji dla statku przeciwnika.
        self.enemy_ship_rect.right = self.container_rect_2.left

        self.container_rect_3 = pygame.Rect(0, 0, 217, 40)
        self.container_rect_3.top = self.container_rect_2.bottom + 20
        self.container_rect_3.x = self.main.screen_width - self.container_rect_3.width - 10

        self.text_3 = str(f'Poziom {self.settings.actual_level}')
        self.font_image_3 = self.font.render(self.text_3, False, self.font_color)
        self.font_rect_3 = self.font_image_3.get_rect()

        self.font_rect_3.center = self.container_rect_3.center

    def blit_life(self):
        """Wyswietla ilosc zyc gracza."""
        self.screen.blit(self.ship_image, self.ship_rect)

    def update_life(self, life):
        """Aktualizuje pozostala liczbe zyc gracza."""
        self.ship_rect.x = 10 + life * (self.ship_rect.width + 10)

    def blit_health_cross(self):
        """Wyswietla obraz krzyza."""
        self.screen.blit(self.health_cross_image, self.health_cross_rect)

    def draw_health_level(self):
        """Wyswietla na ekranie poziom aktualnego zycia gracza."""
        pygame.draw.rect(self.screen, self.font_color, self.container_rect, -1)
        self.screen.blit(self.font_image, self.font_rect)

    def update_health_level(self):
        """Aktualizuje poziom zycia gracza."""
        self.text = str(int(self.main.ship.health))
        self.font_image = self.font.render(self.text, False, self.font_color)

    def how_many_enemies_left_in_game(self):
        """Wyswietla liczbe pozostalych przeciwnikow do pokonania."""
        pygame.draw.rect(self.screen, self.font_color, self.container_rect_2, -1)
        self.screen.blit(self.font_image_2, self.font_rect_2)

    def update_enemies(self):
        """Aktualizuje liczbe pozostalych przeciwnikow do pokonania."""
        self.text_2 = str(self.main.settings.how_many_enemies_left)
        self.font_image_2 = self.font.render(self.text_2, False, self.font_color)

    def blit_enemy_ship_image(self):
        """Wyswietla obraz satku przeciwnika."""
        self.screen.blit(self.enemy_ship_image, self.enemy_ship_rect)

    def blit_actual_level(self):
        pygame.draw.rect(self.screen, self.font_color, self.container_rect_3, -1)
        self.screen.blit(self.font_image_3, self.font_rect_3)

    def update_actual_level(self):
        self.text_3 = str(f'Poziom {self.settings.actual_level}')
        self.font_image_3 = self.font.render(self.text_3, False, self.font_color)

    def reset_ship_health(self):
        """Resetuje poziom zycia gracza."""
        self.main.ship.health = self.ship_health

    def increase_difficult_level(self):
        random_enemies = random.randint(1, 3)

        self.settings.enemy_health += 5

        self.settings.enemy_damage += 1.25

        self.settings.how_many_enemies += random_enemies

        self.settings.enemy_spawn_start -= 25

        self.settings.enemy_spawn_end -= 25
        self.settings.shot_start = 1
        self.settings.shot_end -= 10

        self.settings.star_falling_speed += 0.00625

        self.settings.ammo_speed += 0.025

        self.settings.ship_moving_speed += 0.0375

        self.settings.enemy_moving_speed += 0.025

    def reset_stats(self):
        """Zestaw metod i atrybutow potrzebnych do zresetowania
        rozgrywki po jej zakonczeniu."""
        self.main.ship.center_ship()
        self.main.ship.health = self.ship_health
        self.main.ship.update_health()
        self.main.settings.available_life = self.available_life
        self.main.ammo.empty()
        self.main.enemy_ammo.empty()
        self.main.enemy.empty()
        self.main.settings.enemy_spawned = 0
        self.main._create_enemy()
        self.main._create_enemy_ammo()
        self.main.settings.how_many_enemies_left = self.main.settings.how_many_enemies

        self.main.settings.ship_damage = self.ship_damage
        self.main.settings.ship_defence = self.ship_defence
        self.main.settings.ship_guns = self.ship_guns

        self.main.settings.shooting_frequency = self.shooting_frequency
        self.main.settings.guns_count = self.guns_count
        self.main.settings.ammo_speed = self.ammo_speed
        self.main.settings.enemy_health = self.enemy_health
        self.main.settings.enemy_damage = self.enemy_damage
        self.main.settings.how_many_enemies = self.how_many_enemies
        self.main.settings.how_many_enemies_left = random.randint(1, 5)

        self.main.settings.actual_level = self.actual_level
        self.update_actual_level()

        self.main.settings.star_falling_speed = self.star_falling_speed
