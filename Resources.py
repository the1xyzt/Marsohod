import pygame

class Resources:
    def __init__(self, rx, ry, typee, width, height, ide) -> None:
        self.rx = rx
        self.ry = ry
        self.type = typee
        self.width = width 
        self.height = height
        self.id = ide

    def draw_resource(self, rx, ry, width, height, color,surface):
        rectangle =  pygame.Rect(rx, ry, width, height )
        pygame.draw.rect(surface, color, rectangle, 0)











