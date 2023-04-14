import random
from swarm import Swarm

# Define fitness function
def fitness_func(position):
    return position[0] ** 2

# Set up the swarm
num_particles = 50
dim = 1
bounds = [(-10, 10)]
swarm = Swarm(num_particles, dim, bounds, fitness_func)

# Optimize the function
max_iter = 100
swarm.optimize(max_iter)

# Print the best solution found
print("Best position:", swarm.global_best_position)
print("Best fitness:", swarm.global_best_fitness)

for epoch in swarm.history:
    # plot the swarm at that epoch
    # save as a png
