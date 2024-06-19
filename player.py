import pygame
from constants import *
class Player:
    def __init__(self, mx, my,speed, color, width, height ) -> None:
        self.mx = mx
        self.my = my
        self.speed = speed
        self.color = color
        self.width = width 
        self.height = height

    def draw_player(self, surface):
        rectangel = pygame.Rect(self.mx,self.my, self.width,self.height)
        pygame.draw.rect(surface, self.color, rectangel,0)
        cr_x = self.mx + 10/2
        cr_y = self.my + 10/2
        pygame.draw.circle(surface, "blue", (cr_x, cr_y), RADIUS_OF_VIEW_RESOURCES, 1)

    def player_move(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT] and self.mx < HEIGHT - 10:
            self.mx += PLAYR_SPEED
        if keystate[pygame.K_LEFT] and self.mx >0:
            self.mx -= PLAYR_SPEED    
        if keystate[pygame.K_UP] and self.my > 0:
            self.my -= PLAYR_SPEED
        if keystate[pygame.K_DOWN] and self.my < HEIGHT - 10:
            self.my += PLAYR_SPEED


