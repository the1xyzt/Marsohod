import math 
import pygame
import sys
import random 
import time
from resources import *
from constants import*
import player
import inventori


list_resources = []
invent = inventori.Inventori()

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption(str(clock))
background_image = pygame.image.load('D:/py_proj/Marsohod/Marsohod/textures/background.jpg')
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((500, 500))

player = player.Player(mx,my,PLAYR_SPEED,PLAYER_COLOR,PLAYR_WIDTH,PLAYR_HEIGHT) 
for i in range(3): # Resource spawn 
    list_resources.append(Resources(random.randint(10,400),random.randint(10,400),random.choice(["Au","Ag","Cu"]),resorce_width,resorce_height,core_capacity, True))


def is_resource_in_circle(mx, my, rx, ry ,r):
    distanse = math.sqrt((rx-mx)**2 + (ry-my)**2)
    if distanse <= r:
        return True
    else:
        return False
    
def normalize_coord(coord:int):
    return coord + resorce_height/2


while True:
    screen.blit(background_image, (0, 0))
    clock.tick(FPS)
    for i in list_resources:
        if i.type == "Au":
            i.draw_resource(screen )
        elif i.type == "Ag":
            i.draw_resource(screen )
        elif i.type == "Cu":
            i.draw_resource(screen )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for resource in list_resources:
        if is_resource_in_circle(player.mx,player.my, normalize_coord(resource.rx),normalize_coord(resource.ry), RADIUS_OF_VIEW_RESOURCES) and player.mining_key_is_pressed():
            resource.is_minig = True
            resource.core_capacity -= 1
            if resource.type == "Au":
                invent.sklad["au_count"] +=1
            if resource.type == "Ag":
                invent.sklad["ag_count"] +=1
                invent.sklad["ag_count"] +=1
            if resource.type == "Cu":
                invent.sklad["cu_count"] +=1
                print(invent.sklad["cu_count"])
        if resource.core_capacity == 0:
            list_resources.remove(resource)

    font1 = pygame.font.Font(None, 20)
    text1 = font1.render(str(invent.sklad), True,(0,0,0))



    player.draw_player(screen)
    player.player_move()

    screen.blit(text1, (0,0))
    pygame.display.flip()
    screen.fill((0,0,0))

