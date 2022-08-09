from nonLiving.waste import Waste
from userInterface import *
import random
from object import *

carnivores = []
herbivores = []
plants = []

carnivoresChilds = []
herbivoresChilds = []
seeds = []

objects = wastes + meats
animals = carnivores+ herbivores

class Living:
    def __init__(self,energy,health,sex):
        self.energy= energy
        self.health= health
        self.sex= sex

    def reproduce(self):
        pass

    def inArea(self,radius,objectPosition):
        distance= ((self.position[0]-objectPosition[0])**2+(self.position[1]-objectPosition[1])**2)**0.5
        if distance == 0.0:
            return False
        if distance<=radius:
            return True
        return False

    def eat(self,prey):
        pass

    def energyUpdate(self,index):
        if self.energy >= 1:
            self.energy-=1
        else:
            if self.health >= 20:
                self.energy+=20
                self.health-=20
            else:
                self.health = 0
                
    
    def childBirth(self,addList,babyList,animal):
        if animal.pregnant == 0:
            try:
                position=[0,0]
                position[0] = animal.position[0]
                position[1] = animal.position[1]
                addList.append(animal.__class__(random.choice(['male',"female"]),animal.radiusView,animal.radiusContact,position, energy=self.energyMAX,health=self.healthMAX))
                babyList.remove(animal)
                
            except:
                babyList.remove(animal)
        else:
            animal.pregnant-=1

    def digest(self):
        if self.digestion == 0:
            position = [0,0]
            position[0] = self.position[0]
            position[1] = self.position[1]
            excrement = Waste(300,position)
            wastes.append(excrement)
            objects.append(excrement)
            self.digestion = random.randrange(50,70)
        else:
            self.digestion-=1


