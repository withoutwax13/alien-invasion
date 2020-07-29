import pygame.font

class Label():
    def __init__(self, ai_settings, screen, msg, width, height, x, y):
        """Initialize button attribs"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.msg = msg

        self.width, self.height = width, height
        self.label_color = ai_settings.label_color
        self.text_color = ai_settings.label_text_color
        self.font = pygame.font.Font("fonts/space age.ttf", 15)

        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.label_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
    
    def draw_label(self):
        self.screen.fill(self.label_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)