import random


class Settings:

    def __init__(self, main):
        self.main = main
        self.screen = main.screen

        self.actual_level = 1

        # Ustawienia dotyczace statku.
        self.ship_width = 50
        self.ship_height = 100

        # Predkosc statku.
        self.ship_health = 100
        self.ship_damage = 25
        self.ship_defence = 1
        self.ship_guns = 1
        self.shooting_frequency = 500  # Milisekund

        self.ship_moving_speed = 1
        self.available_life = 3
        self.health_bar_color = (255, 10, 5)

        self.shooting = False
        self.guns_count = 1
        self.ammo_speed = 1

        # Ustawienia dotyczace przeciwnikow.
        self.enemy_health = 50
        self.enemy_damage = 25
        self.enemy_crash = 3 * self.enemy_damage
        self.enemy_moving_speed = 0.2

        self.how_many_enemies = random.randint(1, 5)
        self.how_many_enemies_left = self.how_many_enemies

        self.enemy_spawn_start = 2000
        self.enemy_spawn_end = 10000
        self.spawn_frequency = random.randint(self.enemy_spawn_start, self.enemy_spawn_end)

        self.shot_start = 1
        self.shot_end = 1000
        self.shot_chance = 1
        self.enemy_spawned = 0

        # Ustawienia dotyczace szybkosci opadania gwiazd.
        self.star_falling_speed = 0.4
        self.how_many_stars = 100

        # Ustawienia dotyczace interface menu.
        self.how_to_play = False
        self.menu_active = True
        self.draw_menu_buttons = False
        self.game_active = False
        self.logo_falling_speed = 0.5

        # Ustawienia dotyczace interfacu rozwoju statku.
        self.ship_dev_active = False

    def set_random_spawn(self):
        self.spawn_frequency = random.randint(self.enemy_spawn_start, self.enemy_spawn_end)

    def update_ship_defence(self):
        self.enemy_damage -= self.ship_defence

    def update_actual_level(self):
        self.actual_level = self.main.settings.actual_level
