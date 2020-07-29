import pygame
from settings import Settings

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""

        self.screen = screen
        
        #Load the image and get its rect
        self.image = pygame.image.load("assets/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        #Ship's attributes
        self.ship_speed = Settings().ship_speed_factor
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed
        
        self.rect.centerx = self.center
    
    def centerme(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)