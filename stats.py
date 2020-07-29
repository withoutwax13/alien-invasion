class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_Stats()
        self.game_active = False
        self.is_game_over = False
        self.is_game_paused = False
        self.high_score = self.get_hs()
    
    def reset_Stats(self):
        self.ships_left = self.ai_settings.ship_limit
    
    def set_hs(self, score):
        f = open("hs.txt", "w")
        f.write(str(score))
        f.close()
    
    def get_hs(self):
        f = open("hs.txt", "r")
        score = f.read()
        return int(score)