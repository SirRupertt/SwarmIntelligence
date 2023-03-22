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
    
    def setPos(self, x,y):
        self.x = x
        self.y = y
    
    def setVel(self, velx, vely):
        self.velx = velx
        self.vely = vely
    
    def update(self):
        #U&pdate Vector but need heuristics and ALGO so rn just random
        N=5
        self.velx = random.randint(-N,N)*5
        self.vely = random.randint(-N,N)*5
        #Update Position
        self.x += self.velx
        self.y += self.vely