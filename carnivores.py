from living import *
from object import *
import random
directions = [(-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

class Carnivores(Living):
    def __init__(self,visionRadius,contactRadius):
        self.visionRadius = visionRadius
        self.contactRadius = contactRadius

    def eat(self,prey):
        if self.energy > 0 and self.energy <=100:
            if self.attack >= prey.energy and prey.energy > 0:
                self.energy+=prey.energy
                prey.energy = 0
                return
            if self.attack < prey.energy:
                prey.energy -= self.attack
                self.energy += self.attack
                return
                
    def reproduce(self):
        if len(carnivores) < 200 and len(carnivoresChilds) < 75 and self.strength >= 1 and self.sex == "female":
            carnivoresChilds.append(self)
            self.strength-=1

    def inContactRadius(self,target):
        if target.name == self.name:
            if self.sex != target.sex:
                return self.reproduce()
        return self.eat(target) 
        
    
    def inVisionRadius(self,target):
        distance = (self.position[0]-target.position[0])**2+(self.position[1]-target.position[1])**2
        direct = (0,0)
        for direction in directions:
            newX = self.position[0]+direction[0]*self.speed
            newY = self.position[1]+direction[1]*self.speed
            if (10<newX<(SCREENWIDTH-50)) and (10<newY<(SCREENHEIGHT-50)):
                near = (newX-target.position[0])**2 + (newY-target.position[1])**2 
                if self.attack >=target.attack and near <= distance: 
                    direct = direction
                    distance = near
                if self.attack <=target.attack and near >= distance:
                    direct = direction
                    distance = near
        self.position[0]+=direct[0]*self.speed
        self.position[1]+=direct[1]*self.speed
        return (self.position[0],self.position[1])

    def move(self,directionNumber):
        newX = self.position[0]+directions[directionNumber][0]*self.speed
        newY = self.position[1]+directions[directionNumber][1]*self.speed
        if newX < 10 or newX > (SCREENWIDTH-50) or newY < 10 or newY > (SCREENHEIGHT-50) :
            return self.move(random.randrange(0,8))
        else:
            self.position[0] = newX 
            self.position[1] = newY 
            
        self.digest()
        list = herbivores + meats + carnivores
        random.shuffle(list)
        
        i=0    
        while i<len(list):
            if self.inArea(self.contactRadius,list[i].position) == True:
                self.inContactRadius(list[i])
            if self.inArea(self.visionRadius,list[i].position) == True:
                return self.inVisionRadius(list[i])
            i+=1
        return self.position
    
    
