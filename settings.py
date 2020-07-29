class Settings():
    """A class to store all setings for Alien Invasion"""


    def __init__(self):
        
        #screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.screen_caption = "Space Impact [PATRICK STYLE]"

        #Ship settings
        self.ship_speed_factor = 9
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 5
        self.bullet_height = 7
        self.bullet_color = 0, 0, 255
        self.bullet_num_allowed = 3

        #Alien settings
        self.alien_speed_factor = 9
        self.alien_drop_factor = 10
        self.alien_direction = 1

        #Level settings
        self.level_alien_speed_increase = 0.1
        self.level_alien_drop_increase = 1
        self.level_num = 1

        #Button settings
        self.button_color = 0, 0, 0
        self.button_text_color = 255, 255, 255

        #Label settings
        self.label_color = 0, 0, 0
        self.label_text_color = 255, 255, 255

        
        #Score settings
        self.path = "hs.txt"

        self.scroll_factor = 5
    
    def reset_default(self):
        #Ship settings
        self.ship_speed_factor = 5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 5
        self.bullet_height = 7
        self.bullet_color = 0, 0, 255
        self.bullet_num_allowed = 3

        #Alien settings
        self.alien_speed_factor = 9
        self.alien_drop_factor = 10
        self.alien_direction = 1

        #Level settings
        self.level_alien_speed_increase = 0.1
        self.level_alien_drop_increase = 1
        self.level_num = 1