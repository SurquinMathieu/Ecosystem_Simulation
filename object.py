from userInterface import *
meats=[]
wastes=[]

class Object:
    def __init__(self,energy, position):
        self.energy = energy
        self.position = position
        self.attack = 0
