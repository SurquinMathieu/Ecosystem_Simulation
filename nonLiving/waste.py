import pygame
from object import *

class Waste(Object):
    def __init__(self,energy,position):
        Object.__init__(self, energy, position)
        self.name = "waste"
        self.position = position
        
    
    #sprite
    def draw(self, position):
        
        unsizedWasteImage = pygame.image.load("sprite/waste/waste.png")
        image = pygame.transform.scale(unsizedWasteImage,(25,25))
        screen.blit(image, position)
        
