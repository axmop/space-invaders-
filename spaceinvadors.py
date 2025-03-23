import sys 
import pygame
from settings import Settings 
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group
from alien import Alien
from game_stats import Game_Stats
from button import Button
from scoreboard import Scoreboard
from pygame import mixer


def run_game():
    #initialize game and create a screen object 
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_lenght))
    pygame.display.set_caption('alian invation')
    #make the ship 
    ship = Ship(ai_settings, screen)
    #make a group to stor the bulits in 
    bullets = Group()
    #lets make a group fo alinas as a first step of making the fleet
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)
    #creat an instance to store game statistics and creat scoreboard 
    stats = Game_Stats(ai_settings)
    sb = Scoreboard(ai_settings,screen ,stats)
    #MAKE THE play button 
    play_button = Button(ai_settings, screen, 'play')
    #lets start the main loop for the game 
    
    mixer.music.load("music/background.wav")
    mixer.music.play(-1)
    

    while True:
        #watch for keyboard and mouse events .
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
 aliens, bullets)
        if stats.game_active: 
            ship.update()
            gf.update_bullets(bullets,ai_settings, screen,stats,sb, ship, aliens)
            
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
 bullets)
            #redraw the screen during each pass through the loop 
                    #make the most recently drawn screen visible .
            

        gf.update_screen(ship, bullets, screen, ai_settings, aliens,stats,sb, play_button)
run_game()