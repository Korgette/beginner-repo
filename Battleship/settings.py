class Settings:
    #class for initial settings of battleships(pong)
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (253,222,223)
        self.game_ready = True

        self.ship_speed = 5
        self.ball_speed_x = 0.2
        self.ball_speed_y = 0.2
        self.ball_acceleration = -1.5
        self.ball_max_speed = 1
