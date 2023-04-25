import random
from swarm import Swarm
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import numpy as np

# Define fitness function
def fitness_func(position):
    i = position[0]
    #x^4-5x^2-x+3
    return(i**4-5*i**2-i+3)
    #return position[0] **2

# Set up the swarm
num_particles = 50
dim = 1
bounds = [[-3, 3]]
swarm = Swarm(num_particles, dim, bounds, fitness_func)

# Optimize the function
max_iter = 100
swarm.optimize(max_iter)
arrGen = swarm.getHistory()

# Print the best solution found
print("Best position:", swarm.global_best_position)
print("Best fitness:", swarm.global_best_fitness)

plt.figure(figsize=(10,6))
plt.axes((0,0,10,100))

#plt.scatter(x, y, label = "label_name" )

# Set x and y axes labels
plt.xlabel('X Values')
plt.ylabel('Y Values')

curvex = np.linspace(bounds[0][0], bounds[0][1], 100)
curvey = []

for i in curvex:
    curvey.append(fitness_func([i]))

counter = 0
#Each Gen List 
for epoch in arrGen:
    # plot the swarm at that epoch
    # save as a png
    #Each particle arr in the generation 
    for particle in epoch:
        t=np.linspace(-3,3, 50)
        plt.scatter(particle[0], fitness_func(particle), c=t, cmap="cool")
        plt.figtext(0, .9, "Generation: " + str(counter), fontsize=15)
    plt.axhline(0, color='black', linewidth=.5)
    plt.axvline(0, color='black', linewidth=.5)
    plt.style.use('dark_background')
    #cmap = plt.get_cmap('cool')
    #plt.set_cmap(cmap)
    plt.plot(curvex, curvey)
    plt.xlim(-3,3)
    plt.ylim(-5, 15)
    counter+=1
    print("Image " + str(counter) + " generated.")
    plt.savefig('./images/image' + str(counter) + '.png')
    plt.clf()

# Set the directory containing the PNG files
png_dir = './images'

# Get a list of the PNG files in the directory
png_files = sorted([os.path.join(png_dir, f) for f in os.listdir(png_dir) if f.endswith('.png')], key=os.path.getmtime)

# Create a new imageio writer object for saving the GIF
gif_writer = imageio.get_writer('./images/test.gif', mode='I', duration=0.2)

# Loop over the PNG files and add them to the GIF
for png_file in png_files:
    img = imageio.imread(png_file)
    gif_writer.append_data(img)

# Close the GIF writer to finish saving the file
gif_writer.close()
