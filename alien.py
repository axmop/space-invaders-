import pygame 
from pygame.sprite import Sprite
class Alien(Sprite):
    '''inisialize the alien and set its starting postions '''
    def __init__(self, ai_settings, screen):
        '''initialize the alien and set its starting postion'''    
        super(Alien, self).__init__()
        self.screen = screen 
        self.ai_settings = ai_settings 
        #load alien image and set its rect artibute
        self.image = pygame.image.load("pics/alien.png")
        self.rect = self.image.get_rect()
        #starting each new alien neer the top left 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #stor the alien exact position 
        self.x = float(self.rect.x)
    def blitme(self):
        '''draw the alien at its current postion '''
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        '''return true if the alien at the edg of the screent '''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: 
            return True
        if self.rect.left <= 0:
            return True    
    def update(self):
        '''move the alien right or left'''
        self.x += (self.ai_settings.alien_speed*self.ai_settings.fleet_direction)
        self.rect.x = self.x
    