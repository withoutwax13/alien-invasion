import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to represent the bullets of the Ship"""
    def __init__(self, ai_settings, screen, ship_obj):
        super().__init__()
        self.screen = screen

        #create a bullet rect at (0, 0) and then set correct_position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship_obj.rect.centerx
        self.rect.top = ship_obj.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #Update the decimal position of the bullet
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)