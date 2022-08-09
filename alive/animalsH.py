import pygame
from herbivores import *

class Horse(Herbivores):
    def __init__(self,sex,visionRadius,contactRadius,position, energy=30,health=45):
        Herbivores.__init__(self,visionRadius,contactRadius)
        Living.__init__(self,energy,health,sex)
        self.name = "horse"
        self.energyMax = 30
        self.healthMax = 45
        self.pregnant = 10
        self.digestion = 10
        self.strength = 1
        self.speed = 7 
        self.position = position
        self.attack = self.energy
    
    #sprite
    def draw(self, position):
        
        unsizedHorseImage = pygame.image.load("sprite/horse/horse.png")
        image = pygame.transform.scale(unsizedHorseImage,(50,50))
        screen.blit(image, position)

class Sheep(Herbivores):
    def __init__(self,sex,visionRadius,contactRadius,position, energy=36,health=60):
        Herbivores.__init__(self,visionRadius,contactRadius)
        Living.__init__(self,energy,health,sex)
        self.name = "sheep"
        self.energyMax = 46
        self.healthMax = 60
        self.pregnant = 10
        self.digestion = 10
        self.strength = 1
        self.speed = 10
        self.position = position
        self.attack = self.energy
    
    #sprite
    def draw(self, position):
        
        unsizedSheepImage = pygame.image.load("sprite/sheep/sheep.png")
        image = pygame.transform.scale(unsizedSheepImage,(50,50))
        screen.blit(image, position)

p=0
while p < 8:
    horse1=Horse('male',400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    horse2=Horse("female",400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    herbivores.append(horse1)
    herbivores.append(horse2)

    sheep1=Sheep('male',400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    sheep2=Sheep("female",400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    herbivores.append(sheep1)
    herbivores.append(sheep2)
    p+=1