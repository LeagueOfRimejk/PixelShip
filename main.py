import os.path
import time

import pygame

import sys

import random

from background import Background
from button import Button
from settings import Settings
from ship import Ship
from game_background import GameBackground
from game_logo import GameLogo
from in_game_menu import InGameMenu
from ammo import Ammo
from enemy_ship import Enemy
from enemy_ammo import EnemyAmmo
from game_stats import GameStats
from ship_development_menu import ShipDevelopmentMenu
from sounds import Sounds
from how_to_play import HowToPlay


# noinspection PyTypeChecker
class Main:
    """Glowna klasa gry przeznaczona do zarzadzania jej zasobami."""

    def __init__(self):
        """Inicializacja atrybutow."""
        # Inicializacja pygame.
        pygame.init()

        # Czas potrzebny do dzialania niektorych metod.
        self.start = pygame.time.get_ticks()
        self.start2 = pygame.time.get_ticks()
        self.start3 = pygame.time.get_ticks()
        self.start4 = pygame.time.get_ticks()
        self.start5 = pygame.time.get_ticks()
        self.start6 = pygame.time.get_ticks()
        self.start7 = pygame.time.get_ticks()

        # Wymiary ekranu.
        self.screen = pygame.display.set_mode((1200, 800), pygame.HWSURFACE)

        # Nazwa okna gry.
        pygame.display.set_caption('Pixel Ship', 'Pixel_ship')

        # Ikonka gry.
        icon_path = 'resources/images/ship/'
        self.game_icon = pygame.image.load(os.path.join(
            icon_path, 'new_ship.png')).convert_alpha()

        self.game_icon = pygame.transform.rotate(self.game_icon, 45)
        pygame.display.set_icon(self.game_icon)

        # Szerokosc, wysokosc ekranu.
        self.screen_width, self.screen_height = self.screen.get_rect().size

        # Egzemplarz ustawien.
        self.settings = Settings(self)

        # Egzemplarz tla w menu.
        self.bg = Background(self)

        # Egzemplarz tla w trakcie gry.
        self.stars = pygame.sprite.Group()

        # Egzemplarz statku.
        self.ship = Ship(self)

        # Grupa amunicji.
        self.ammo = pygame.sprite.Group()
        self.ammo_left = pygame.sprite.Group()
        self.ammo_right = pygame.sprite.Group()

        # Grupa przeciwnikow.
        self.enemy = pygame.sprite.Group()

        # Grupa pociskow przeciwnika.
        self.enemy_ammo = pygame.sprite.Group()

        # Statystyki gry.
        self.stats = GameStats(self)

        # Grupa kol.
        self.circles = pygame.sprite.Group()

        # Zaladowanie obrazu tla menu.
        self.background = pygame.image.load(os.path.join(
            'resources/images/background/', 'background.jpg')).convert()

        # Utworzenie egzemplarza loga gry.
        self.game_logo = GameLogo(self)

        # Utworzenie egzemplarza dzwiekow gry.
        self.sounds = Sounds(self)

        self.how_to_play = HowToPlay(self)

        # Tworzy Interface menu.
        self.buttons = pygame.sprite.Group()
        self._create_menu_buttons(['Graj', 'Jak grac', 'Wyjdz'])

        # Tworzy interface menu w trakcie gry.
        self.in_game_buttons = pygame.sprite.Group()
        self._create_in_game_buttons(['Wznow', 'Restart', 'Wyjdz'],
                                     (self.screen_width - 300) / 2,
                                     (self.screen_height - 70) / 2)

        # Tworzy interface dla rozwoju statku.
        self.ship_dev_menu = ShipDevelopmentMenu(self)
        self.ship_dev_buttons = pygame.sprite.Group()

        self.dev_buttons = ['Atak +5', 'Obrona +1', 'Zycie +25', 'Szybkosc ataku +0.01', 'Nowa bron +1']
        self._create_ship_dev_buttons(self.dev_buttons,
                                      self.ship_dev_menu.rect2.right - self.ship_dev_menu.rect.width,
                                      self.ship_dev_menu.rect2.top)

        self.sounds.main_menu_sound()

    def start_game(self):
        """Uruchamia gre."""
        # Glowna petla gry.
        while True:
            # Sprawdza zdarzenia uzytkownika.
            self._events_check()

            # Aktualizuje ekran gry.
            self._screen_update()

    def _create_menu_buttons(self, names_render, pos_x=50, pos_y=500):
        """Tworzy przyciski intefejsu menu."""

        for name in names_render:
            # Iteracja przez liste przyciskow do utworzenia.
            # Przypisanie im tekstu wyswietlanego w argumencie 'names_render'.

            string = f'button_{name}'
            string = Button(self, name, pos_x, pos_y)
            pos_y += string.rect.height + 20

            self.buttons.add(string)

    def _create_in_game_buttons(self, names_render, pos_x=50, pos_y=100):
        """Tworzy przyciski menu w trakcie gry."""

        for name in names_render:
            # Iteracja przez liste przyciskow do utworzenia.
            # Przypisanie im tekstu wyswietlanego w argumencie 'names_render'.

            string = f'button_{name}'
            string = InGameMenu(self, name, pos_x, pos_y)
            pos_y += string.rect.height + 20

            self.in_game_buttons.add(string)

    def _create_ship_dev_buttons(self, names_render, pos_x=50, pos_y=100):
        """Tworzy przyciski rozwoju statku w trakcie gry."""
        for name in names_render:
            # Iteracja przez liste przyciskow do utworzenia.
            # Przypisanie im tekstu wyswietlanego w argumencie 'names_render'.

            string = f'button_{name}'
            string = ShipDevelopmentMenu(self, name, pos_x, pos_y)
            pos_y += string.rect.height + 20

            self.ship_dev_buttons.add(string)

    def _events_check(self):
        """Monitoruje zdarzenia dokonywane przez uzytkownika."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Wyjscie z programu.
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Dla wcisnietych klawiszy.
                self._keydown_event(event)

            if event.type == pygame.KEYUP:
                # Dla niewcisnietych klawiszy.
                self._keyup_events(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Dla przycisku myszy.
                x, y = pygame.mouse.get_pos()
                self._mousebutton_down(x, y)

    def _mousebutton_down(self, mouse_pos_x, mouse_pos_y):
        """Reakcje dla wcisnietego klawisza myszy.
        Monitorowanie polozenia kursora."""
        # Menu gry.
        if self.settings.menu_active:

            for button in self.buttons:

                if pygame.Rect.collidepoint(button.rect, (mouse_pos_x, mouse_pos_y)):

                    if button.text == 'Graj':
                        self.sounds.in_game_sound()

                        self.settings.menu_active = False
                        self.settings.game_active = True
                        self.settings.how_to_play = False

                    elif button.text == 'Jak grac':
                        self.settings.how_to_play = True

                    elif button.text == 'Wyjdz':
                        sys.exit()

            if self.settings.how_to_play:
                if pygame.Rect.collidepoint(self.how_to_play.quit, (mouse_pos_x, mouse_pos_y)):
                    self.settings.how_to_play = False

        # Podczas rozgrywki.
        if not self.settings.game_active and not self.settings.menu_active:

            for button in self.in_game_buttons:

                if pygame.Rect.collidepoint(button.rect, (mouse_pos_x, mouse_pos_y)):

                    if button.text == 'Wznow':
                        self.settings.game_active = True

                    elif button.text == 'Restart':

                        self.settings.menu_active = False
                        self.settings.game_active = True
                        self.stats.reset_stats()

                    elif button.text == 'Wyjdz':
                        self.settings.game_active = False
                        self.circles.empty()
                        self.stars.empty()
                        self.settings.menu_active = True
                        self.game_logo.blit_logo_again()
                        self.stats.reset_stats()
                        self.sounds.stop_play_list()
                        self.sounds.main_menu_sound()
                        for next_buttons in self.buttons:
                            next_buttons.blit_menu_buttons_again()

        # Podczas zakonczenia poziomu.
        if self.settings.ship_dev_active:
            for button in self.ship_dev_buttons:
                if pygame.Rect.collidepoint(button.rect, (mouse_pos_x, mouse_pos_y)):

                    if button.text == 'Atak +5':
                        self.settings.ship_damage += 5
                        self._next_level()
                        self.settings.ship_dev_active = False

                    if self.settings.enemy_damage - self.settings.ship_defence > 0:
                        if button.text == 'Obrona +1':
                            self.settings.ship_defence += 1
                            self.settings.update_ship_defence()
                            self._next_level()
                            self.settings.ship_dev_active = False

                    if button.text == 'Zycie +25':
                        self.settings.ship_health += 25
                        self._next_level()
                        self.settings.ship_dev_active = False

                    if self.settings.shooting_frequency > 100:
                        if button.text == 'Szybkosc ataku +0.01':
                            self.settings.shooting_frequency -= 10
                            self._next_level()
                            self.settings.ship_dev_active = False

                    if button.text == 'Nowa bron +1':
                        if self.settings.ship_guns < 3:

                            if (
                                    self.settings.actual_level >= 6 and
                                    self.settings.ship_guns == 1 or
                                    self.settings.actual_level >= 12 and
                                    self.settings.ship_guns == 2
                            ):
                                self.settings.ship_guns += 1
                                self._next_level()
                                self.settings.ship_dev_active = False

    def _next_level(self):
        self.stats.increase_difficult_level()
        self.ship.health_level_up()
        self.settings.how_many_enemies_left = self.settings.how_many_enemies
        self.settings.enemy_spawned = 0
        self.settings.actual_level += 1
        self.stats.update_actual_level()

    def _keydown_event(self, event):
        """Monitorowanie zdarzen dla wcisnietych klawiszy."""
        # Wyjscie z programu poprzez wcisniecie 'X' w prawym
        # gornym rogu ekranu.
        if event.key == pygame.K_q:
            sys.exit()

        # Zatrzymanie rozgrywki.
        if event.key == pygame.K_ESCAPE:
            self.settings.game_active = False

        # Poruszanie sie statku.
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        # Strzelanie.
        if event.key == pygame.K_SPACE:
            self.settings.shooting = True

    def _keyup_events(self, event):
        """Monitorowanie zdarzen dla niewcisnietych klawiszy."""
        # Poruszanie sie statku.
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        # Strzelanie.
        if event.key == pygame.K_SPACE:
            self.settings.shooting = False

    def _shoot(self):
        """Tworzy egzemplarz pocisku i dodaje go do grupy 'self.ammo'."""
        # Czas potrzebny do wystrzelenia kolejnego przycisku.
        self.how_many_ammo = pygame.time.get_ticks()

        # Egzemplarz amunicji.
        new_ammo = Ammo(self)
        if self.settings.shooting:
            if self.how_many_ammo - self.start2 > self.settings.shooting_frequency:
                self.ammo.add(new_ammo)
                self.sounds.laser_sound()
                self.start2 = self.how_many_ammo

    def _shoot_left_gun(self):
        # Czas potrzebny do wystrzelenia kolejnego przycisku.
        self.how_many_ammo2 = pygame.time.get_ticks()

        # Egzemplarz amunicji.
        new_ammo_left = Ammo(self)
        new_ammo_left.rect.left = self.ship.rect.left
        new_ammo_left.y += 70
        if self.settings.shooting:
            if self.how_many_ammo2 - self.start6 > self.settings.shooting_frequency - 100:
                self.ammo_left.add(new_ammo_left)
                self.sounds.laser_sound()
                self.start6 = self.how_many_ammo2

    def _shoot_right_gun(self):
        # Czas potrzebny do wystrzelenia kolejnego przycisku.
        self.how_many_ammo3 = pygame.time.get_ticks()

        # Egzemplarz amunicji.
        new_ammo_right = Ammo(self)
        new_ammo_right.rect.right = self.ship.rect.right
        new_ammo_right.y += 70
        if self.settings.shooting:
            if self.how_many_ammo3 - self.start7 > self.settings.shooting_frequency - 50:
                self.ammo_right.add(new_ammo_right)
                self.sounds.laser_sound()
                self.start7 = self.how_many_ammo3

    def _update_ammo(self):
        """Aktualizuje i wyrysowuje na ekranie pocisk."""
        for ammo in self.ammo:
            ammo.update()
            ammo.draw_rect()

            # Jesli pocisk pojawi sie poza ekranem, usuwa go.
            if ammo.rect.bottom < 0:
                self.ammo.remove(ammo)

        if self.settings.ship_guns >= 2:
            for ammo_left in self.ammo_left:
                ammo_left.update()
                ammo_left.draw_rect()

                if ammo_left.rect.bottom < 0:
                    self.ammo_left.remove(ammo_left)

        if self.settings.ship_guns >= 3:
            for ammo_right in self.ammo_right:
                ammo_right.update()
                ammo_right.draw_rect()

                if ammo_right.rect.bottom < 0:
                    self.ammo_right.remove(ammo_right)

    def _add_circles(self):
        """Tworzy nowe kola dla tla ekranu."""
        self.spawn = pygame.time.get_ticks()
        # Egzemplarz kola.
        new_circle = Background(self)

        if len(self.circles) < self.bg.how_many_circles:
            if self.spawn - self.start >= 1380:
                self.start = self.spawn
                self.circles.add(new_circle)

    def _remove_circle(self, circle):
        """Usuwa nadmiar kol."""
        if (
                (
                        circle.circle_x < -circle.circle_radius or circle.circle_x >
                        self.screen.get_rect().width + circle.circle_radius) or

                (
                        circle.circle_y < -circle.circle_radius or circle.circle_y >
                        self.screen.get_rect().height + circle.circle_radius)

        ):
            self.circles.remove(circle)
            # Ustala limit odbic i liczby kol na ekranie.
            circle.how_many_bounces = self.bg.get_random_number(5, 25)
            self.bg.how_many_circles = self.bg.get_random_number(1, 20)

    def _update_circles(self):
        """Aktualizacja polozenia kol."""
        self.circles.update()
        # Tworzy nowe kola, ustala ich kierunek poruszania, jesli potrzeba
        # usuwa nadmiar kol.
        for circle in self.circles:
            self._remove_circle(circle)
            circle.change_circle_direction()
            circle.draw_circle()

    def _create_game_background_object(self):
        """Tworzy egzemplarz klasy GameBackground definiujacy nowe gwiazdy
        do tla rozgrywki i dodaje je do grupy 'self.stars'."""
        # Utworzenie egzemplarza.
        new_star = GameBackground(self)
        if len(self.stars) < new_star.how_many_stars:
            self.stars.add(new_star)

    def _update_game_background(self):
        """Iteruje przez grupe 'self.stars' aktualizuje pozycje gwiazdy
        na ekranie i ja wyrysowuje."""
        for star in self.stars:
            star.star.y = -star.star.height
            # Aktualizacja i wyrysowanie.
            star.update()
            star.draw_rect()

            if star.star.top >= self.screen.get_rect().height:
                self.stars.remove(star)

    def _blit_game_logo(self):
        """Wyswietla na ekranie logo i nazwe gry."""
        self.game_logo.update_logo()
        self.game_logo.blit_logo()

    def _blit_menu_buttons(self):
        """Wyswietla na ekranie interface menu."""
        # Iteruje przez grupe 'self.buttons' uaktualnia pozycje
        # i wyrysowuje przycisk na ekranie.
        for button in self.buttons.sprites():
            button.update()
            button.draw_rect()

    def _blit_in_game_buttons(self):
        """Wyswietla na ekranie interface menu."""
        # Iteruje przez grupe 'self.buttons' uaktualnia pozycje
        # i wyrysowuje przycisk na ekranie.
        for button in self.in_game_buttons.sprites():
            button.update()
            button.draw_rect()

    def _blit_ship_dev_buttons(self):
        for button in self.ship_dev_buttons:
            if button.text != 'Nowa bron +1':
                button.update()
                button.draw_rect()
            else:
                if self.settings.actual_level >= 6 and self.settings.ship_guns == 1:
                    button.update()
                    button.draw_rect()
                elif self.settings.actual_level >= 12 and self.settings.ship_guns == 2:
                    button.update()
                    button.draw_rect()

    def _create_enemy(self):
        """Tworzy egzemplarz przeciwnika i dodaje go do grupy przecinikow."""
        # Czestotliwosc dodawania przeciwnikow.
        self.spawn_enemy = pygame.time.get_ticks()

        if self.settings.enemy_spawned < self.settings.how_many_enemies:
            if self.spawn_enemy - self.start4 > self.settings.spawn_frequency:
                # Egzemplarz.
                new_enemy = Enemy(self)
                # Wywolanie metody odpowiadajacej za
                # losowosc tworzenia przeciwnikow.
                self.settings.set_random_spawn()
                self.enemy.add(new_enemy)
                # Monitorowanie utworzonych przeciwnikow.
                self.settings.enemy_spawned += 1

                self.start4 = self.spawn_enemy

    def _update_enemy(self):
        """Aktualizuje i wyrysowuje wszystkich przeciwnikow z grupy."""
        # Iteracja przez grupe przeciwnikow.
        for enemy in self.enemy.sprites():
            enemy.update_enemy()
            enemy.blit_enemy()
            enemy.draw_enemy_health()

            # Wykrywanie kolizji pomiedzy przeciwnikiem a amunicja gracza.
            self._check_collision_between_enemy_player_ammo(enemy)

            # Wykrywanie kolizji pomiedzy statkiem przeciwnika,
            # a statkiem gracza.
            self._check_collision_between_enemy_ship_player_ship(enemy)

            if enemy.rect.top > self.screen_height:
                # Jesli przeciwnik opusci ekran, usuniecie egzemplarza.
                self.enemy.remove(enemy)
                # Odjecie zycia graczowi.
                self.settings.available_life -= 1
                self.settings.how_many_enemies_left -= 1

    def _check_collision_between_enemy_player_ammo(self, enemy):
        """Wykrywa kolizje pocisku gracza z przeciwnikiem."""
        if pygame.sprite.spritecollide(enemy, self.ammo, True):
            # Dekrementacja punktow zycia przeciwnika o
            # wartosc wskazana w ship_damage.
            self.sounds.get_hit_sound()
            enemy.enemy_health -= self.settings.ship_damage
            enemy.update_enemy_health()

        if pygame.sprite.spritecollide(enemy, self.ammo_left, True):
            self.sounds.get_hit_sound()
            enemy.enemy_health -= self.settings.ship_damage
            enemy.update_enemy_health()

        if pygame.sprite.spritecollide(enemy, self.ammo_right, True):
            self.sounds.get_hit_sound()
            enemy.enemy_health -= self.settings.ship_damage
            enemy.update_enemy_health()

        # Jesli zycie przeciwnika rowne badz mniejsze od zera,
        # usuniecie egzemplarza przeciwnika.
        if enemy.enemy_health <= 0:
            self.enemy.remove(enemy)
            self.sounds.enemy_crash_sound()
            self.settings.how_many_enemies_left -= 1

    def _check_collision_between_enemy_ship_player_ship(self, enemy):
        """Wykrywa kolizcje pomiedzy statkiem przeciwnika, a statkiem gracza."""
        if pygame.sprite.spritecollideany(self.ship, self.enemy):
            self.enemy.remove(enemy)
            self.sounds.enemy_crash_sound()
            self.settings.how_many_enemies_left -= 1

            self.ship.health -= self.settings.enemy_crash

            # Korekta, aby po spadku zycia gracza ponizej 0
            # byla wyswietlana wartosc 0.
            if self.ship.health < 0:
                self.sounds.player_crash_sound()
                self.ship.health = 0

            # Aktualizacja zycia gracza.
            self.ship.update_health()

    def _create_enemy_ammo(self):
        """Tworzy egzemplarz amunicji przeciwnika."""
        # Szansa na trafienie w zakresie liczb losowych.
        chance = random.randint(self.settings.shot_start, self.settings.shot_end)
        if self.enemy:
            if chance == self.settings.shot_chance:
                # Utworzenie egzemplarza pocisku.
                new_enemy_ammo = EnemyAmmo(self)
                self.enemy_ammo.add(new_enemy_ammo)
                self.sounds.enemy_laser_sound()

    def _update_enemy_ammo(self):
        """Aktualizacja i wyrysowanie amunicji przeciwnika."""
        for ammo in self.enemy_ammo.sprites():
            # Iteracja przez grupe amunicji.
            ammo.update_ammo()
            ammo.draw_ammo()

            if ammo.rect.top > self.screen_height:
                # Jesli amunicja opusci ekran gry,
                # usuwana jest z grupy amunicji.
                self.enemy_ammo.remove(ammo)

            # Wykrywanie kolicji pomiedzi pociskiem przeciwnika, a graczem.
            self._check_collision_between_player_enemy_ammo(ammo)

    def _check_collision_between_player_enemy_ammo(self, ammo):
        """Wykrywa kolizje pomiedzy amunicja przeciwnika, a graczem."""
        if pygame.sprite.spritecollideany(self.ship, self.enemy_ammo):
            self.sounds.get_hit_sound()

            # Usuniecie egzemplarza amunicji
            self.enemy_ammo.remove(ammo)

            self.ship.health -= self.settings.enemy_damage
            if self.ship.health < 0:
                self.sounds.player_crash_sound()
                self.ship.health = 0

            # Aktualizacja zycia gracza.
            self.ship.update_health()

    def _update_in_game_interface(self):
        """Aktualizacja i wyrysowanie interfacu podczas gry."""
        # Utworzenie obrazu statkow w liczbe wskazanej w avaiable_life.
        for life in range(self.settings.available_life):
            self.stats.blit_life()
            self.stats.update_life(life)

        self.stats.blit_health_cross()
        self.stats.update_health_level()
        self.stats.draw_health_level()
        self.stats.how_many_enemies_left_in_game()
        self.stats.update_enemies()
        self.stats.blit_enemy_ship_image()
        self.stats.blit_actual_level()

    def _create_ship_development_interface(self):
        if self.settings.how_many_enemies_left <= 0:
            self.settings.ship_dev_active = True

        self.ship_dev_menu.create_surface_for_ship_dev()
        self.ship_dev_menu.create_ship_stats()
        self._blit_ship_dev_buttons()

    def _screen_update(self):
        """Aktualizuje ekran."""
        # Ukrycie kursora.
        if self.settings.game_active and not self.settings.ship_dev_active:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)

        # Jesli liczba dostepnych zyc spadnie do 0, nastepuje koniec gry.
        if self.settings.available_life < 0:
            self.settings.game_active = False

        # Jesli gra jest aktywna.

        if self.settings.game_active:

            # Jesli zycie spadnie ponizej 0, dekrementacja
            # dostepnych zyc gracza.
            if self.ship.health <= 0:
                self.settings.available_life -= 1
                time.sleep(2)
                self.stats.reset_ship_health()
                self.ship.update_health()
                self.ship.center_ship()

            # Wypelnia ekran gry.
            self.screen.fill((0, 0, 0))

            # Tworzy tlo dla rozgrywki.
            self._create_game_background_object()
            self._update_game_background()

            # Aktualizacja polozenie statku.
            self.ship.update_ship()

            # Wyswietlenie statku.
            self.ship.blit_ship()

            # Wyswietla pasek zycia statku.
            self.ship.draw_health()
            self.ship.update_health()

            # Dodanie egzemplarzy pociskow do grupy 'self.ammo'.
            if self.settings.shooting:
                self._shoot()
                if self.settings.ship_guns >= 2:
                    self._shoot_left_gun()
                if self.settings.ship_guns >= 3:
                    self._shoot_right_gun()

            # Wyrysowanie i aktualizacja pociskow.
            self._update_ammo()

            # Utworzenie egzemplarzy przeciwnikow.
            self._create_enemy()

            # Aktualizacja i wyrysowanie przeciwnikow.
            self._update_enemy()

            # Utworzenie amunicji przeciwnika.
            self._create_enemy_ammo()

            # Aktualizacja i wyrysowanie pociskow przeciwnika.
            self._update_enemy_ammo()

            # Aktualizacja InterFace'u podaczas gry.
            self._update_in_game_interface()

            if self.settings.how_many_enemies_left <= 0:
                self.ship_dev_menu.update_ship_stats()
                self._create_ship_development_interface()

        else:
            # Utworzenie i wyswietlenie przyciskow menu w trakcie gry.
            self._blit_in_game_buttons()

        # Jesli menu gry jest aktywne.
        if self.settings.menu_active:
            # Wyswietlenie obrazu tla.
            self.screen.blit(self.background, (0, 0))

            # Tworzy nowe kolo.
            self._add_circles()

            # Aktualizuje polozenie kol.
            self._update_circles()

            # Utworzenie i aktualizacja loga gry i nazwy gry.
            self._blit_game_logo()

            # Utworzenie i wyswietlenie przyciskow menu.
            self._blit_menu_buttons()

            # Wyswietlenie samouczka.
            if self.settings.how_to_play:
                self.how_to_play.blit_how_to_play()

        # Przejscie do nowego ekranu.
        pygame.display.flip()


# Utworzenie egzemplarza gry.
if __name__ == '__main__':
    m = Main()
    m.start_game()
