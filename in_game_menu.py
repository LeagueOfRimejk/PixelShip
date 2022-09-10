import pygame

import pygame.font

from button import Button


class InGameMenu(Button):
    """Klasa glowna definiujaca menu interface w trakcie gry."""
    def __init__(self, main, text='', pos_x=50, pos_y=500):
        """Inicializacja atrybutow oraz dziedziczenie 'super()'."""
        super().__init__(main, text, pos_x, pos_y)

        # Polozenie startowe nowych przyciskow.
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 300, 70)

    def update(self):
        """Aktualizuje polozenie przyciskow na srodku ekranu."""
        self.font_rect.center = self.rect.center
