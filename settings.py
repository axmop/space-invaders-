class Settings():
    '''a class to store all settings for alian invasion'''
    def __init__(self):
        """initialize game statistics settings """
        #screen settings 
        self.screen_width = 1200
        self.screen_lenght = 700
        self.bg_color = (230,230,230)
        #SHIP settings 
        self.speed_ship = 9
        #bullets settings 
        self.bullet_speed = 9
        #limiting the player emo 
        self.number_of_bullets = 50
        #alien settings 
        self.alien_speed = 3
        self.drop_speed = 10
        #setting the fleet direction 1 is right -1 is left 
        self.fleet_direction = 1
        self.ship_limit = 3
        #how quickly the game speed up 
        self.speed_up_factor = 1.1
         # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        '''initialize the settings that change through out the game '''
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 3
        self.bullet_speed_factor = 1
        #fleet direction 1 represent right -1 represent left
        self.fleet_direction = 1
        #scoring 
        self.alien_points = 50
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speed_up_factor
        self.alien_speed_factor *= self.speed_up_factor
        self.bullet_speed_factor *= self.speed_up_factor
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


        