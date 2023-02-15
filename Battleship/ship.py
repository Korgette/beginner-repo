import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #class governing ship
    def __init__(self,bs_game):
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.screen_rect = bs_game.screen.get_rect() #set rect for screen
        self.width,self.height = 50,120
        self.ship_color = (0,0,255)

        self.rect = pygame.Rect(200,50,self.width,self.height) #draw rect @0,0
        self.rect.midleft = self.screen_rect.midleft #move bottom to bottom of screen

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def draw_ship(self):
        #draw the ship on screen at current position
       pygame.draw.rect(self.screen,self.ship_color,self.rect) #draw rect


    def update(self):
        #update ship position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        
        #update collision rect
        self.rect.x = self.x
        self.rect.y = self.y
        
        
        
