import random
from swarm import Swarm
import matplotlib.pyplot as plt
import imageio
import os

# Define fitness function
def fitness_func(position):
    return position[0] ** 2

# Set up the swarm
num_particles = 50
dim = 2
bounds = [(-10, 10), (-10, 10)]
swarm = Swarm(num_particles, dim, bounds, fitness_func)

# Optimize the function
max_iter = 100
arrGen = swarm.optimize(max_iter)

# Print the best solution found
print("Best position:", swarm.global_best_position)
print("Best fitness:", swarm.global_best_fitness)

plt.figure(figsize=(10,6))
#plt.scatter(x, y, label = "label_name" )

# Set x and y axes labels
plt.xlabel('X Values')
plt.ylabel('Y Values')

counter = 0
#Each Gen List 
for epoch in arrGen:
    # plot the swarm at that epoch
    # save as a png
    #Each particle arr in the generation 
    for particle in epoch:
        plt.scatter(particle[0], particle[1])
    counter+=1
    plt.savefig('images/image' + str(counter) + '.png')
    plt.clf()

png_dir = "C:\Users\Drew\Documents\GitHub\SwarmIntelligence\temp\images"
images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))

# Make it pause at the end so that the viewers can ponder
#for _ in range(10):
#    images.append(imageio.imread(file_path))

imageio.mimsave('movie.gif', images)