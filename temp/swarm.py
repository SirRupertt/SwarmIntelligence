from particle import Particle
import numpy as np

class Swarm:
    def __init__(self, num_particles, dim, bounds, fitness_func, w=0.5, c1=0.5, c2=0.7):
        self.num_particles = num_particles
        self.dim = dim
        self.bounds = bounds
        self.fitness_func = fitness_func
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.global_best_position = []
        self.global_best_fitness = float('inf')
        self.particles = []
        # ArrGen, ArrParticles, Arr Positions

        for i in range(num_particles):
            particle = Particle(dim, bounds)
            self.particles.append(particle)
            if particle.best_fitness < self.global_best_fitness:
                self.global_best_fitness = particle.best_fitness
                self.global_best_position = particle.best_position[:]
        self.history = [self.get_particles_positions()]
    
    def get_particles_positions(self):
        return np.array([particle.position for particle in self.particles])
        

    def optimize(self, max_iter):
        #ArrGen contains lists of each generation
        #Each gen in arrGen contains ArrPos
        #ArrPos contains arrays of x,y pairs of particle coordinates
        for i in range(max_iter):
            for particle in self.particles:
                particle.evaluate(self.fitness_func)
                if particle.best_fitness < self.global_best_fitness:
                    self.global_best_fitness = particle.best_fitness
                    self.global_best_position = particle.best_position[:]
            for particle in self.particles:
                particle.update_velocity(self.global_best_position, self.w, self.c1, self.c2)
                particle.update_position(self.bounds)
            self.history.append(self.get_particles_positions())

    def getHistory(self):
        print(self.history)
        return(self.history)