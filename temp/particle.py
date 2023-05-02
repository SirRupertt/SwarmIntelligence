import random
import numpy as np

class Particle:
    def __init__(self, dim, bounds):
        self.position = []
        self.velocity = []
        self.best_position = []
        self.fitness = float('inf')
        self.best_fitness = float('inf')

        for i in range(dim):
            self.position.append(random.uniform(bounds[i][0], bounds[i][1]))
            self.velocity.append(random.uniform(-1, 1))

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position = np.clip(self.position + self.velocity, bounds[i][0], bounds[i][1])

    def update_velocity(self, global_best_position, w, c1, c2):
        for i in range(len(self.velocity)):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1 * r1 * (self.best_position[i] - self.position[i])
            social = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive + social

    def evaluate(self, fitness_func):
        self.fitness = fitness_func(self.position)
        if self.fitness < self.best_fitness:
            self.best_fitness = self.fitness
            self.best_position = self.position[:]
