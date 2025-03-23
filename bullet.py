import pygame
from pygame.sprite import Sprite
from ship import Ship
class Bullet(Sprite):
    '''a class manage bulites fired from the ship '''
    number_bullets = 5
    def __init__(self, ai_settings, ship, screen):
        '''creat a bulit object at the ship current position'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.bullet_image = pygame.image.load('pics/two.png')
        self.rect = self.bullet_image.get_rect()
        #creat a bulit rect at 0,0 and then set the correct positon 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store the bulits position at decimal value 
        self.y = float(self.rect.y) 
        self.speed = ai_settings.bullet_speed
    def update(self):
        '''move the bulit up the screen '''
        #update the decimal position 
        self.y -= self.speed
        #update the rect postion 
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw the bulit to the screen '''
        self.screen.blit(self.bullet_image, self.rect)