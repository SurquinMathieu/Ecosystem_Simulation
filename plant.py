from object import *
from living import *
import random
class Plant(Living):
    def __init__(self,rootRadius,sowingRadius):
        self.sowingRadius=sowingRadius
        self.rootRadius=rootRadius
    
    def eat(self,waste): 
        if self.energy > 0 and waste.energy > 0:
            self.energy += 20
            waste.energy -= 20
            return
       
                
    def reproduce(self,x,y):
        if len(plants)<50 and self.strength >= 1 and self.energy <= 10:
            child=self.__class__(150,10,300,100,position=[x,y])
            seeds.append(child)
            self.strength -= 1

    def inRootArea(self,elem):
        i=0
        while i<len(elem):
            element = elem[i]
            if self.inArea(self.rootRadius,element.position)==True:
                if type(element).__name__ == 'Waste':
                    return self.eat(element)
            i+=1
    
    def inSowingArea(self):
        x = self.position[0] + random.randrange(-self.sowingRadius,self.sowingRadius)
        y = self.position[1] + random.randrange(-self.sowingRadius,self.sowingRadius)
        if x < 10 or x > (SCREENWIDTH-50) or y < 10 or y > (SCREENHEIGHT-50) :
            return self.inSowingArea()
        else:
            return self.reproduce(x,y)
        
