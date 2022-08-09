import pygame
from object import *

class Meat(Object):
    def __init__(self,energy,position):
        Object.__init__(self,energy, position)
        self.name = "meat"
        self.position = position
        self.attack = 0
    
    #sprite
    def draw(self, position):       
        unsizedMeatImage = pygame.image.load("sprite/meat/meat.png")
        image = pygame.transform.scale(unsizedMeatImage,(25,25))
        screen.blit(image, position)