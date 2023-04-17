from particle import Particle

class Swarm:
    def __init__(self, num_particles, dim, bounds, fitness_func, w=0.729, c1=1.49445, c2=1.49445):
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
        self.history = []

        for i in range(num_particles):
            particle = Particle(dim, bounds)
            self.particles.append(particle)
            if particle.best_fitness < self.global_best_fitness:
                self.global_best_fitness = particle.best_fitness
                self.global_best_position = particle.best_position[:]

    def optimize(self, max_iter):
        #ArrGen contains lists of each generation
        #Each gen in arrGen contains ArrPos
        #ArrPos contains arrays of x,y pairs of particle coordinates
        arrGen = []
        for i in range(max_iter):
            arrPos = []
            for particle in self.particles:
                particle.evaluate(self.fitness_func)
                if particle.best_fitness < self.global_best_fitness:
                    self.global_best_fitness = particle.best_fitness
                    self.global_best_position = particle.best_position[:]
            for particle in self.particles:
                particle.update_velocity(self.global_best_position, self.w, self.c1, self.c2)
                particle.update_position()
                arrPos.append(particle.getPos())
            arrGen.append(arrPos)
        return(arrGen)
