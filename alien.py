import pygame
import sys
import game_functions as gf
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        
        #Load the image and get its rect
        self.image = pygame.image.load("assets/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def update(self, stats, ship, aliens, ai_settings, screen, bullets):
        """Move the alien right"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.alien_direction
        self.rect.x = self.x


    def check_edges(self):
        if self.rect.x > self.screen_rect.right or self.rect.x < self.screen_rect.left:
            return True
        return False
    
    def blitme(self):
        #Draw alien at current position
        self.screen.blit(self.image, self.rect)
    