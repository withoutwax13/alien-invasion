import pygame
from settings import Settings

class Background():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""

        self.screen = screen
        
        #Load the image and get its rect
        self.image = pygame.image.load("assets/background.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new background at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self, ai_settings):
        self.rect.bottom -= ai_settings.scroll_factor
        if self.rect.bottom == self.screen_rect.top:
            self.rect.bottom = self.screen_rect.bottom