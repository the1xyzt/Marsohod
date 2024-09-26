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
        self.gold_texture = pygame.image.load('D:/py_proj/Marsohod/Marsohod/textures/gold_ore.jpg').convert_alpha()
        self.silver_texture = pygame.image.load('D:/py_proj/Marsohod/Marsohod/textures/ag_ore.jpg').convert_alpha()
        self.copper_texture = pygame.image.load('D:/py_proj/Marsohod/Marsohod/textures/cuprum_ore(s).png').convert_alpha()
        
    def draw_resource(self, screen):
        # Создаем поверхность с альфа-каналом
        surface = pygame.Surface((self.rectangle.width, self.rectangle.height), pygame.SRCALPHA)

        # Полностью прозрачный фон
        surface.fill((0, 0, 0, 0))

        # Выбираем текстуру в зависимости от типа ресурса
        if self.type == "Au":
            surface.blit(self.gold_texture, (0, 0))
        elif self.type == "Ag":
            surface.blit(self.silver_texture, (0, 0))
        elif self.type == "Cu":
            surface.blit(self.copper_texture, (0, 0))

        # Рисуем поверхность на экране
        screen.blit(surface, self.rectangle)










