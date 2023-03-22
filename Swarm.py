import Agent
import random

class Swarm:
    def __init__(self):
        self.swarm = []
        for i in range(10):
            #Create particle
            N = 5
            self.swarm.append(Agent.Agent((random.randint(0,N)*100), (random.randint(0,N)*100), (random.randint(-N,N)*5), (random.randint(-N,N)*5)))

    def getVel(self):
        for i in self.swarm:
            return
        
    def getSwarm(self):
        return(self.swarm)
    
    def update(self):
        for i in self.swarm:
            i.update()