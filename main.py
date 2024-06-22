import math 
import pygame
import sys
import random 
import time
from resources import *
from constants import*
import player


list_resources = []


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption(str(clock))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = player.Player(mx,my,PLAYR_SPEED,PLAYER_COLOR,PLAYR_WIDTH,PLAYR_HEIGHT) 
for i in range(3): # Resource spawn 
    list_resources.append(Resources(random.randint(10,400),random.randint(10,400),random.choice(["Au","Ag","Cu"]),RESOURCE_WIDTH,RESOURCE_HEIGHT,core_capacity, True))


def is_resource_in_circle(mx, my, rx, ry ,r):
    distanse = math.sqrt((rx-mx)**2 + (ry-my)**2)
    if distanse <= r:
        return True
    else:
        return False
    
def normalize_coord(coord:int):
    return coord + RESOURCE_HEIGHT/2



while True:
    clock.tick(FPS)
    for i in list_resources:
        if i.type == "Au":
            i.draw_resource( Au_color,screen )
        elif i.type == "Ag":
            i.draw_resource(Ag_color,screen )
        elif i.type == "Cu":
            i.draw_resource(Cu_color,screen )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for resource in list_resources:
        if is_resource_in_circle(player.mx,player.my, normalize_coord(resource.rx),normalize_coord(resource.ry), RADIUS_OF_VIEW_RESOURCES):
            resource.is_minig = True
            resource.core_capacity -= 1
        if resource.core_capacity == 0:
            list_resources.remove(resource)

    player.draw_player(screen)
    player.player_move()

    pygame.display.flip()
    screen.fill((0,0,0))

