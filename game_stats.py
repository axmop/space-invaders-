class Game_Stats():
    '''for tracking the game statistics '''
    def __init__(self,ai_settings):
        '''Initialize statistics.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        #start the game in inactive mode 
        self.game_active = False
         # High score should never be reset.
        self.high_score = 0
    def reset_stats(self):
        '''initialize statistics that can be changed during the game '''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 
        self.level = 1


        