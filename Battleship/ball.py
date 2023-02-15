import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
#class for managing ball
    
    def __init__(self,bs_game):
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.screen_rect = bs_game.screen.get_rect()
        self.width = 2.5
        self.height = 2.5
        self.radius = 5
        self.ball_color = (255,6,0)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        ##Redundant - use negative accel to reverse ball
        #self.right = False
        #self.left = False
        #self.up = False
        #self.down = False
        #self.x_move = False

    def draw_ball(self):
        pygame.draw.circle(self.screen,self.ball_color,
                           (self.x,self.y),self.radius)





    def check_x_edges(self):
        #check if ball hits left side of screen
         screen_rect = self.screen.get_rect()
         if self.rect.left <=0:
             if self.settings.ball_speed_x >= self.settings.ball_max_speed:
                 self.settings.ball_acceleration = -1
             self.settings.ball_speed_x *= self.settings.ball_acceleration
         if self.rect.right >= screen_rect.right:
             if self.settings.ball_speed_x >= self.settings.ball_max_speed:
                 self.settings.ball_acceleration = -1
             self.settings.ball_speed_x *= self.settings.ball_acceleration

    def check_y_edges(self):
        #check if ball hits right side of screen
        screen_rect = self.screen.get_rect()
        if self.rect.top <=0:
            if self.settings.ball_speed_y >= self.settings.ball_max_speed:
                 self.settings.ball_acceleration = -1
            self.settings.ball_speed_y *= self.settings.ball_acceleration
        if self.rect.bottom >= screen_rect.bottom:
            if self.settings.ball_speed_y >= self.settings.ball_max_speed:
                 self.settings.ball_acceleration = -1
            self.settings.ball_speed_y *= self.settings.ball_acceleration
      
        
    def update(self):
        #update balls position
        if self.x_move == True:
            self.x += self.settings.ball_speed_x
        if self.y_move == True:
            self.y += self.settings.ball_speed_y

        #align collision rect with current location
        self.rect.x = self.x
        self.rect.y = self.y


            

    
        

    
