class Settings:
    
    def __init__(self):
        """initialize game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
       
        #ship setting
        self.ship_speed = 10
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 8
        self.bullet_height = 20
        self.bullet_color = (255,163,67)
        self.bullets_allowed = 30

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5

        #how quickly game speeds up
        self.speedup_scale = 1.1

        #how quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize setttings that change throughout the game"""
        self.ship_speed = 10
        self.bullet_speed = 10.0
        self.alien_speed = 1.0

        #fleet direction of 1 represents right and -1 the left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)