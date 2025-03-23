import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        '''initialize button artibutes'''
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        #set the button dimentions 
        self.width, self.hight = 50,100
        self.button_color = (0,255,0)    
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,45)
        #build the button rect and centering it 
        self.rect = pygame.Rect(0,0,self.hight,self.width)
        self.rect.center = self.screen_rect.center 
        #the button massage need to appear only once 
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        '''turn text into rendered msg and center the text on the screen '''
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        #draw blank button and  then draw the message 
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    