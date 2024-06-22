import pygame

class Resources:
    def __init__(self, rx, ry, typee, width, height,core_capacity ,is_mining):
        self.rx = rx
        self.ry = ry
        self.type = typee
        self.width = width 
        self.height = height
        self.core_capacity = core_capacity
        self.is_mining = is_mining

    def draw_resource(self, color,surface):
        rectangle =  pygame.Rect(self.rx, self.ry, self.width, self.height )
        pygame.draw.rect(surface, color, rectangle, 0)











