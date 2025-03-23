import pygame
from pygame.sprite import Sprite



class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        '''initialize the ship and set its starting position.'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #lead the ship image and get its rect 
        self.image = pygame.image.load('pics/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #flaf movement 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


        #start each ship at the bottom center of the screen .
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store decimal value for shipes center 
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
    def update(self):
        '''apdate the movement of the ship based on the movment of the flag '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.speed_ship 
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.speed_ship  
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.speed_ship 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            self.bottom += self.ai_settings.speed_ship
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom  

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        '''center the ship on the screen '''
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom