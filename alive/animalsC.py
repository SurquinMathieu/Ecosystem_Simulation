import pygame
from carnivores import *

class Cheetah(Carnivores):
    def __init__(self,sex,visionRadius,contactRadius,position,energy = 45,health = 90):
        Carnivores.__init__(self,visionRadius,contactRadius)
        Living.__init__(self,energy,health,sex)
        self.name = "cheetah"
        self.energyMax = 45
        self.healthMax = 90
        self.pregnant = 100
        self.digestion = 500
        self.strength = 1
        self.speed = 7
        self.position = position
        self.attack = self.energy
    
    #sprite
    def draw(self, position):      

        unsizedCheetahImage = pygame.image.load("sprite/cheetah/cheetah.png")
        image = pygame.transform.scale(unsizedCheetahImage,(50,50))
        screen.blit(image, position)


class Bear(Carnivores):
    def __init__(self,sex,visionRadius,contactRadius,position,energy = 120,health = 135):
        Carnivores.__init__(self,visionRadius,contactRadius)
        Living.__init__(self,energy,health,sex)
        self.name = "bear"
        self.energyMax = 120
        self.healthMax = 135
        self.pregnant = 50
        self.digestion = 300
        self.speed = 8
        self.strength = 1
        self.position = position
        self.attack = self.energy
        
    def draw(self, position):       
        unsizedBearImage = pygame.image.load("sprite/bear/bear.png")
        image = pygame.transform.scale(unsizedBearImage,(50,50))
        screen.blit(image, position)

p=0
while p < 8:
    cheetah1=Cheetah('male',300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    cheetah2=Cheetah("female",300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    
    bear1=Bear('male',300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    bear2=Bear("female",300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    carnivores.append(cheetah1)
    carnivores.append(cheetah2)
    carnivores.append(bear1)
    carnivores.append(bear2)
    p+=1


