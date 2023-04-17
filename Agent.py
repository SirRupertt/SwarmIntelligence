import random
import numpy as np

class Agent():
    def __init__(self, pos, vel):
        self.particle = [pos]
        self.vel = [vel]
    
    def getPos(self):
        return(self.particle)
    
    def getVel(self):
        return(self.vel)
    
    def setPos(self, pos):
        self.particle = pos
    
    def setVel(self, vel):
        self.vel = vel

    #Finds new velocity of particle
    def update_velocity(particle, velocity, pbest, gbest, w_min=0.5, max=1.0, c=0.1):
        #Init new velocity array
        num_particle = len(particle)
        new_velocity = np.array([0.0 for i in range(num_particle)])
        #Randomly generate r1, r2 and inertia weight from normal distributaion
        r1=random.uniform(0,max) #random impulses to velocity 
        r2=random.uniform(0,max)
        w=random.uniform(w_min,max) #Inertia weight
        c1=c #constant acceleration values
        c2=c
        #Calc new velocity per particle
        for i in range(num_particle):
            new_velocity[i] = w*velocity[i] + c1*r1*(pbest[i]-particle[i])+c2*r2*(gbest[i]-particle[i]) 
            #First part is inertia force, then individual particle best vector then global best vector
        return(new_velocity)

    def update(self):
        #U&pdate Vector but need heuristics and ALGO so rn just random
        N=5
        self.velx = random.randint(-N,N)*5
        self.vely = random.randint(-N,N)*5
        #Adds vel to pos of particle 
        # Move particles by adding velocity
        new_particle = self.particle + self.vel
        return new_particle