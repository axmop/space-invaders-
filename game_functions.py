import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
from pygame import mixer 
def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
 bullets):
#resopond to key press and mouse events 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship, bullets, screen, ai_settings)

        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
 aliens, bullets, mouse_x, mouse_y)
def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
 aliens, bullets, mouse_x, mouse_y):
    '''start a new game when the player click play ''' 
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)  
    if button_clicked and not stats.game_active:
        #reset the game settings 
        ai_settings.initialize_dynamic_settings()
        #making the mouse cursor visible 
        pygame.mouse.set_visible(False)
        #reset the statistics when ever u click on the play button 
        stats.reset_stats()
        stats.game_active = True
         # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #empty the the list fo aliens and bullets 
        aliens.empty()
        bullets.empty()
        #creat a new fleet and center the ship 
        create_fleet(ai_settings, screen, ship, aliens)
def check_keydown(event, ship, bullets, screen, ai_settings):
    '''resnode to keypresses'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        #creet a bullet and add it to the bullet group 
        bullet_firing(ship, bullets, screen, ai_settings)
        mixer.music.load("music/laser.wav")
        mixer.music.play()

    if event.key == pygame.K_q:
        sys.exit()
def check_keyup(event,ship):
    '''resposnce to keyreleases '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
def update_screen(ship, bullets, screen, ai_settings, aliens,stats,sb, play_button):
    '''update image on the screen and flip to the new screen '''

#redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    back = pygame.image.load("pics/planet-6215636_1280.jpg")
    screen.blit(back,(0,0))
        #redraw all the bullets behind the ship and alian
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #make the alien showen 
    aliens.draw(screen)
    #draw the score information 
    sb.show_score()
    #draw the button when the game is inactive mode 
    if not stats.game_active:
        play_button.draw_button()
#make the mose recent drawn screen visible
    pygame.display.flip()
def update_bullets(bullets,ai_settings, screen,stats,sb, ship, aliens):
    '''update the bullets postion and deleting the old bullets'''
    bullets.update()
        #get rid of the bullit that passed the screen 
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collesion(bullets,ai_settings, screen,stats,sb, ship, aliens)
    
def bullet_firing(ship, bullets, screen, ai_settings):
    '''fire bulit if the limit is not reached yet '''
    if len(bullets) < ai_settings.number_of_bullets :
            new_bullet = Bullet(ai_settings,ship,screen)
            bullets.add(new_bullet)
def create_fleet(ai_settings, screen, ship, aliens):
    '''creat a full fleet of aliens '''
    #create an aline and find how many  aliens can fit in a row 
    #space one alien space between each alien and the other
    alien = Alien(ai_settings, screen)
    number_aliensx = get_x_alien_number(ai_settings, alien.rect.width)
    number_row = get_y_alien_number(ai_settings, ship.rect.height, alien.rect.height)
    #creat first line of the aliens 
    for row_number in range(number_row):
        for alien_number in range(number_aliensx):
        #creat an alien and place it in a row 
            creat_aliens(alien_number, ai_settings, screen, aliens, row_number)
def get_x_alien_number(ai_settings, alien_width):
    available_spacex = ai_settings.screen_width - (3*alien_width)
    number_aliensx = int(available_spacex/(3*alien_width))
    return number_aliensx
def get_y_alien_number(ai_settings,ship_height,alien_height):
    '''determin the number of rows that can fit of the screenc'''
    available_spacey = ai_settings.screen_lenght - (4*alien_height)- ship_height
    number_rows = int(available_spacey/(3*alien_height))
    return number_rows
def creat_aliens(alien_number, ai_settings, screen, aliens, row_number):
    #creat an alien and place it in a row 
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    alien.rect.x = alien.x 
    aliens.add(alien)
def check_fleet_edg(ai_settings,aliens):
    '''respond appropriately if the aliens reached the edgs '''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    '''drop the entire fleet and change the fleet direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.drop_speed
    ai_settings.fleet_direction *=-1
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''check if the alians at the edg then update the position of aliens'''
    check_fleet_edg(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        print('ship hit !!!!')
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #look for the aliens hiting the bottom of the screen 
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
def check_bullet_alien_collesion(bullets,ai_settings, screen,stats,sb, ship, aliens):
    '''check the colision   if so get rid of the bulit and the colision'''
    collision = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            mixer.music.load("music/explosion.wav")
            mixer.music.play()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        '''when the last alien fall we creat a new fleet and destroy the existing bullets and speed up the game '''
        # If the entire fleet is destroyed, start a new level
        # Increase level.
        stats.level += 2
        sb.prep_level()
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''responce to the ship being hit by the alien'''
    if stats.ships_left> 0:
        #decrement the ship_left
        stats.ships_left -=1
        # Update scoreboard. 
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        #create a new fleet and center the ship 
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #pause
        sleep(0.5)
    else :
        stats.game_active = False   
        pygame.mouse.set_visible(True) 
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
 bullets):
    '''check if aliens has reached the bottom of the screen'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #treat this as the same as if the ship got hit 
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
 