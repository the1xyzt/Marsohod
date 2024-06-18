import math 
import pygame
import sys
import random 
import time
from Resources import *

WIDTH = 500
HEIGHT = 500
FPS = 60

mx = 100
my = 100
rx = 150
ry = 150

speed = 5

resources = []
Cu_color = (184, 115, 5)
Au_color = (255, 215, 0)
Ag_color = (192, 192, 192)

Cu_Width, Cu_Height = 10, 10
Au_Width, Au_Height = 10, 10
Ag_Width, Ag_Height = 10, 10

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption(str(clock))

screen = pygame.display.set_mode((WIDTH, HEIGHT))


for i in range(3):
    resources.append(Resources(random.randint(10,400),random.randint(10,400),random.choice(["Au","Ag","Cu"]),20,20,str(i)))




def draw_player(mx,my):
    rectangel = pygame.Rect(mx,my, 10, 10)
    pygame.draw.rect(screen, (100,100,100), rectangel,0)


def calculate_coord_circle(mx, my):
    cr_x = mx + 10/2
    cr_y = my + 10/2
    return cr_x, cr_y

def draw_circle(mx,my):
    pygame.draw.circle(screen, "blue", (calculate_coord_circle(mx,my)), 20, 1)


def is_resource_in_circle(mx, my, rx, ry ,r):
    distanse = math.sqrt((rx-mx)**2 + (ry-my)**2)
    if distanse <= r:
        return True
    else:
        return False 


while True:
    clock.tick(FPS)
    for i in resources:
        if i.type == "Au":
            i.draw_resource(i.rx, i.ry, 20,20, Au_color,screen )
        elif i.type == "Ag":
            i.draw_resource(i.rx, i.ry,20,20, Ag_color,screen )
        elif i.type == "Cu":
            i.draw_resource(i.rx, i.ry,20,20, Cu_color,screen )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT] and mx < HEIGHT - 10:
        mx += speed
    if keystate[pygame.K_LEFT] and mx >0:
        mx -= speed    
    if keystate[pygame.K_UP] and my > 0:
        my -= speed
    if keystate[pygame.K_DOWN] and my < HEIGHT - 10:
        my += speed
    
    for i in resources:
        # print(is_resource_in_circle(mx,my,i["rx"], i["ry"], 20))
        if is_resource_in_circle(mx,my,i["rx"], i["ry"], 20):
            i["is_mining"] = True
        elif is_resource_in_circle(mx,my,i["rx"], i["ry"], 20) == False:
            i["is_mining"] = False


    draw_player(mx,my)   
    draw_circle(mx,my)
    # for i in resources:
    #     if i["is_mining"] == True:
    #         print(i)
    #         if i["type"] == "Cu":
    #             Cu_Width -= 0.01
    #             Cu_Height -= 0.01
    #         if i["type"] == "Au":
    #             Au_Width -= 0.01
    #             Au_Height -= 0.01
    #         if i["type"] == "Ag":
    #             Ag_Width -= 0.01
    #             Ag_Height -= 0.01

    pygame.display.flip()
    screen.fill((0,0,0))

