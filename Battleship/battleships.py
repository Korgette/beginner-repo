#Very original Battleships(tm)
#(its definitely not a half baked battleship idea reworked into pong)

#To do:
#Add lives/scoring system, on ball hitting puck add score(multiple of speed)
#on ball hitting left side, remove one life

#Lessons:
#keep functions handling objects in the same space(ball accel is all over place)
#

import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from ball import Ball

class BattleShips:
    #class to manage game assets
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))
        pygame.display.set_caption('Battleships')
        self.ship = Ship(self)
        self.ball = Ball(self)
       


    def update_screen(self):
        #Function updating screen with asset positions
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        self.ball.draw_ball()
        pygame.display.flip()

    def run_game(self):
        #init ball movement, main loop for game
        self.ball.x_move = True
        self.ball.y_move = True
        while True:
            self.ball_check()
            self.check_events()
            self.ship.update()
            self.update_screen()

    def check_events(self):
        #check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:
                self.check_keydowns(event)
            elif event.type == pygame.KEYUP:
                self.check_keyups(event)

    def check_keydowns(self,event):
        #check for key presses, start movement in corresponding direction
       
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
##redundant - this ship has only vertical thrusters!
##         if event.key == pygame.K_RIGHT:
##            self.ship.moving_right = True
##        elif event.key == pygame.K_LEFT:
##            self.ship.moving_left = True

    def check_keyups(self,event):
        #check for keyups, stop movement
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

#redundant - this ship has only vertical thrusters!
##        if event.key == pygame.K_RIGHT:
##            self.ship.moving_right = False
##        elif event.key == pygame.K_LEFT:
##            self.ship.moving_left = False
         


    def ball_check(self):
        #update the ball, check for collisions with the ship
        self.ball.update()
        self.ball.check_x_edges()
        self.ball.check_y_edges()
        if self.ball.rect.colliderect(self.ship.rect):
            if self.settings.ball_speed_x >= self.settings.ball_max_speed or self.settings.ball_speed_y >= self.settings.ball_max_speed:
                self.settings.ball_acceleration = -1
            self.settings.ball_speed_x *= self.settings.ball_acceleration
            self.settings.ball_speed_y *= self.settings.ball_acceleration
        


if __name__ =='__main__':
    bs = BattleShips()
    bs.run_game()
