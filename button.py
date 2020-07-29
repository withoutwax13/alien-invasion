import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attribs"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.width, self.height = 250, 50
        self.button_color = ai_settings.button_color
        self.text_color = ai_settings.button_text_color
        self.font = pygame.font.Font("fonts/space age.ttf", 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)