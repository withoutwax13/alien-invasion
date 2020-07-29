import pygame
import sys
from time import sleep
from bullets import Bullet
from alien import Alien
from label import Label

def check_events(ai_settings, stats, screen, ship_obj, aliens, bullets, play_button):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(ai_settings, event, ship_obj, bullets, screen, stats, aliens)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship_obj, bullets)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(stats, play_button, mouse_x, mouse_y, ship_obj, aliens, bullets, ai_settings, screen)

def check_play_button(stats, play_button, mouse_x, mouse_y, ship, aliens, bullets, ai_settings, screen):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_Stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens)
        ship.centerme()
        
        pygame.mouse.set_visible(False)

def check_keydown_events(ai_settings, event, ship_obj, bullets, screen, stats, aliens):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship_obj.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship_obj.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship_obj, bullets)
    elif event.key == pygame.K_p:
        if stats.game_active and not stats.is_game_paused:
            stats.game_active = False
            stats.is_game_paused = True
        elif not stats.game_active:
            if stats.is_game_paused:
                stats.game_active = True
                stats.is_game_paused = False
            elif not stats.is_game_paused:
                stats.game_active = True
            if stats.is_game_over:
                stats.reset_Stats()
                stats.high_score = ai_settings.level_num
                ai_settings.reset_default()
                stats.game_active = True
                aliens.empty()
                bullets.empty()
                create_fleet(ai_settings, screen, aliens)
                ship_obj.centerme()
                sleep(0.5)


def check_keyup_events(event, ship_obj, bullets):
    if event.key == pygame.K_RIGHT:
        ship_obj.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship_obj.moving_left = False
    elif event.key == pygame.K_SPACE:
        #do nothing
        pass


def update_screen(settings, stats, screen, bg, bg2, ship, aliens, bullets, play_button, game_over_label,game_paused_label):
    screen.fill(settings.bg_color)
    bg.update(settings)
    bg2.update(settings)
    bg.blitme()
    bg2.blitme()

    set_highscore(settings, stats)

    if not stats.game_active and not stats.is_game_over and stats.is_game_paused:
        game_paused_label.draw_label()
    elif not stats.game_active and stats.is_game_over and not stats.is_game_paused:
        game_over_label.draw_label()
    elif not stats.game_active and not stats.is_game_over and not stats.is_game_paused:
        play_button.draw_button()

    life = "Ships: " + str(stats.ships_left)
    level = "Level " + str(settings.level_num)
    high_score = "Record: " + str(stats.high_score)
    high_score_label = Label(settings, screen, high_score, 100, 50, 250, 0)
    level_label = Label(settings, screen, level, 100, 50, 0, 0)
    lifeline_label = Label(settings, screen, life, 100, 50, 500, 0)
    lifeline_label.draw_label()
    level_label.draw_label()
    high_score_label.draw_label()
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()

def set_highscore(settings, stats):
    if settings.level_num > stats.high_score:
        stats.set_hs(settings.level_num)
        stats.high_score = stats.get_hs()

def update_bullets(bullets, aliens, ai_settings, screen):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_alien_bullet_alien_collisions(bullets, aliens, ai_settings, screen)

def check_alien_bullet_alien_collisions(bullets, aliens, ai_settings, screen):
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.alien_speed_factor += ai_settings.level_alien_speed_increase
        ai_settings.alien_drop_factor += ai_settings.level_alien_drop_increase
        ai_settings.level_num += 1
        create_fleet(ai_settings, screen, aliens)

def update_aliens(aliens, ship, ai_settings, stats, screen, bullets):
    aliens.update(stats, ship, aliens, ai_settings, screen, bullets)
    check_fleet_edges(aliens, ai_settings)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, ship, aliens, ai_settings, screen, bullets)
    for alien in aliens.sprites():
        if alien.rect.bottom > screen.get_rect().bottom:
            bottom_hit(stats, ship, aliens, ai_settings, screen, bullets)
            break

def ship_hit(stats, ship, aliens, ai_settings, screen, bullets):
    if stats.ships_left > 0:
        print("Ship hit!")
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens)
        ship.centerme()
        sleep(0.5)
        
    else:
        if ai_settings.level_num > stats.high_score:
            stats.set_hs(ai_settings.level_num)
            stats.high_score = stats.get_hs()
        stats.is_game_over = True
        stats.game_active = False

def bottom_hit(stats, ship, aliens, ai_settings, screen, bullets):
    if stats.ships_left > 0:
        print("Bottom hit!")
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens)
        ship.centerme()
        sleep(0.5)
        
    else:
        if ai_settings.level_num > stats.high_score:
            stats.set_hs(ai_settings.level_num)
            stats.high_score = stats.get_hs()
        stats.is_game_over = True
        stats.game_active = False


def fire_bullet(ai_settings, screen, ship_obj, bullets):
    #ADD NEW BULLET AND ADD IT TO BULLET GROUP
    if len(bullets) < ai_settings.bullet_num_allowed:
        if ai_settings.level_num % 10 == 0:
            ai_settings.bullet_width = 150
        elif ai_settings.level_num % 15 == 0:
            ai_settings.bullet_width = 200
        elif ai_settings.level_num % 5 == 0:
            ai_settings.bullet_width = 50
        else:
            ai_settings.bullet_width = 5
        new_bullet = Bullet(ai_settings, screen, ship_obj)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.x
    alien_height = alien.y

    available_space_x = ai_settings.screen_width - (2 * alien_width)
    available_space_y = ai_settings.screen_height - (3 * alien_height)        
    number_aliens_x = (available_space_x / (2 * alien_width))
    number_aliens_y = (available_space_y / (4 * alien_height))

    for alien_num_y in range(int(number_aliens_y)):
        for alien_num_x in range(int(number_aliens_x)):
            alien_ind = Alien(ai_settings, screen)
            alien_ind.x = alien_width + 2 * alien_width * alien_num_x
            alien_ind.y = alien_height + 2 * alien_height * alien_num_y
            alien_ind.rect.x = alien_ind.x
            alien_ind.rect.y = alien_ind.y
            aliens.add(alien_ind)

def check_fleet_edges(aliens, ai_settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break

def change_fleet_direction(aliens, ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_factor
    ai_settings.alien_direction *= -1