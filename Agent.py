import random

class Agent():
    def __init__(self, x, y, velx, vely):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
    
    def getPos(self):
        return([self.x, self.y])
    
    def getVel(self):
        return([self.velx, self.vely])
    
    def Update(self):
        #Increase by vector
        self.x += self.velx
        self.y += self.vely
        #Randomize new vector
        N=5
        self.velx = random.randint(-N,N)*5
        self.vely = random.randint(-N,N)*5