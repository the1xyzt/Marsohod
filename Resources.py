import pygame
from constants import *
class Resources:
    def __init__(self, rx, ry, typee, width, height,core_capacity ,is_mining):
        self.rx = rx
        self.ry = ry
        self.type = typee
        self.width = width 
        self.height = height
        self.core_capacity = core_capacity
        self.is_mining = is_mining
        self.rectangle = pygame.Rect(self.rx, self.ry, self.width, self.height )
        self.cu_texture = pygame.image.load("textures/cuprum.jpg")
    def draw_resource(self, color,surface):
        pygame.draw.rect(surface, color, self.rectangle, 0)
        self.cu_texture  = pygame.transform.scale(self.cu_texture, (self.rectangle.width, self.rectangle.height))











