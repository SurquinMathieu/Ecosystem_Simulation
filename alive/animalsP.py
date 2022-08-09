import pygame
from plant import *

class Fern(Plant):
    def __init__(self,energy,health,rootRadius,sowingRadius,position):
        Plant.__init__(self,rootRadius,sowingRadius)
        Living.__init__(self,energy,health,sex='')
        self.name = "fern"
        self.strength = 5
        self.position = position
    
    #sprite
    def draw(self, position):
        unsizedFernImage = pygame.image.load("sprite/fern/fern.png")
        image = pygame.transform.scale(unsizedFernImage,(25,25))
        screen.blit(image, position)

p=0
while p < 30:
    fern1=Fern(15,10,300,100,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    plants.append(fern1)
    p+=1 