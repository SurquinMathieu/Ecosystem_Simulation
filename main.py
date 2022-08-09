import pygame, sys,random
from pygame.locals import *
from userInterface import *

from living import *
from alive.animalsC import *
from alive.animalsH import *
from alive.animalsP import *

from object import *
from nonLiving.meat import *
from nonLiving.waste import *

from plant import *

class Main:
    pygame.init()

    FPS = 0

    image = pygame.image.load("background/terrain.jpg")
            
    #Initialisation
    while 1:
        for event in pygame.event.get():
            if event.type== QUIT: #if pressing the X, quit the program
                pygame.quit() #stop pygame
                sys.exit() #stop the program
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit() #stop the program
        screen.blit(image, (0,0))
        
        # 1er = plants
        toKill = []
        toAdd = []
        plant = 0
        while plant<len(plants):
            plants[plant].draw(plants[plant].position)
            plants[plant].energyUpdate(plant)
            if plants[plant].health <= 0:
                toKill.append(plant)
                toAdd.append([plant, plants[plant].position])
            plants[plant].inRootArea(wastes)
            plants[plant].inSowingArea()
            plant+=1
        for dead in reversed(toKill):
            plants.remove(plants[dead]) 
        for i, position in toAdd:
            wastes.append(Waste(300, position))
            objects = wastes + meats

        
        #2eme animaux
        toKill = []
        toAdd = []
        i=0
        while i<len(animals): #update all animals
            newPosition=animals[i].move(random.randrange(0,8))
            animals[i].draw(newPosition)
            animals[i].energyUpdate(i)
            if animals[i].health <= 0:
                toKill.append(i)
                toAdd.append([i, animals[i].position])
            i+=1

        for dead in reversed(toKill):
            try:
                carnivores.remove(animals[dead])
            except:
                herbivores.remove(animals[dead])
            animals.remove(animals[dead])
        for i, position in toAdd:
            meat = Meat(300, position)
            meats.append(meat)
            objects.append(meat)


        #3eme objets
        toKill = []
        toAdd = []
        objet = 0
        while objet<len(objects): #update all objects
            objects[objet].draw(objects[objet].position)
            if objects[objet].energy >= 1:
                objects[objet].energy-=1  
                
            else:
                toKill.append(objet)
                if (isinstance(objects[objet], Waste)) == False:
                    toAdd.append([objet, objects[objet].position])
            objet+=1
            
        for dead in reversed(toKill):
            try:
                meats.remove(objects[dead])
            except:
                wastes.remove(objects[dead])
            objects.remove(objects[dead])
            

        for i, position in toAdd:
            wastes.append(Waste(300, position))
            objects = wastes + meats
        
        #childBirth
        for herbivoresChild in herbivoresChilds:
            herbivoresChild.childBirth(herbivores,herbivoresChilds,herbivoresChild)
        for carnivoresChild in carnivoresChilds:
            carnivoresChild.childBirth(carnivores,carnivoresChilds,carnivoresChild)


        animals = carnivores + herbivores
        plants+=seeds
        seeds.clear()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)
