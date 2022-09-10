import pygame
import os.path


class HowToPlay:
    def __init__(self, main):
        self.main = main
        self.screen = main.screen

        htp = 'resources/images/how_to_play/'

        self.image = pygame.image.load(os.path.join(htp, 'how_to_play.png')).convert_alpha()
        self.htp_rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.htp_rect.width, self.htp_rect.height - 150))

        self.htp_rect = self.image.get_rect()

        self.htp_rect.bottom = self.screen.get_rect().bottom
        self.htp_rect.right = self.screen.get_rect().right

        self.quit = pygame.Rect(0, self.htp_rect.y, 50, 50)
        self.quit.x = self.htp_rect.x + self.htp_rect.width - self.quit.width

        self.quit_cross_image = pygame.image.load(os.path.join(htp, 'quit_cross.png'))
        self.quit_cross_rect = self.quit_cross_image.get_rect()
        self.quit_cross_rect.center = self.quit.center

    def blit_how_to_play(self):
        self.screen.blit(self.image, self.htp_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), self.quit, 5)
        self.screen.blit(self.quit_cross_image, self.quit_cross_rect)
