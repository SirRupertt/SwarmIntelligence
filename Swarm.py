import Agent
import random

#Define Fitness Function
#f(x,y)=(x-2y+3)^2+(2x+y-8)^2
#Find 0 minimum is the goal

def fitness_function(x1,x2):
    f1=x1+2*-x2+3
    f2=2*x1+x2-8
    z = f1**2+f2**2
    return(z)

#Running the Program
population = 100
dimension = 2
position_min = -100.0
position_max = 100.0
generation = 400
fitness_criterion = 10e-4

#pso_2d(population, dimension, position_min, position_max, generation, fitness_criterion)

class Swarm:
    def __init__(self):
        self.swarm = []
        for i in range(10):
            #Create particle
            N = 5
            self.swarm.append(Agent.Agent((random.randint(0,N)*100), (random.randint(0,N)*100), (random.randint(-N,N)*5), (random.randint(-N,N)*5)))
        # Particle's best position
        pbest_position = self.swarm
        # Fitness
        pbest_fitness = [fitness_function(p[0],p[1]) for p in self.swarm]

    def getVel(self):
        for i in self.swarm:
            return
        
    def getSwarm(self):
        return(self.swarm)
    
    def update(self):
        for i in self.swarm:
            i.update()