import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from stats import GameStats
from button import Button
from label import Label
from background import Background
from background2 import Background2

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)
    bg = Background(screen)
    bg2 = Background2(screen)
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    game_over_label = Label(ai_settings, screen, "Game Over! Play again!", 250, 50, 175, 300)
    game_paused_label = Label(ai_settings, screen, "Game Paused", 250, 50, 175, 300)
    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(ai_settings, stats, screen, ship, aliens, bullets, play_button)
        if stats.game_active == True:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen)
            gf.update_aliens(aliens, ship, ai_settings, stats, screen, bullets)
        gf.update_screen(ai_settings, stats, screen, bg, bg2, ship, aliens, bullets, play_button, game_over_label, game_paused_label)
        

run_game()