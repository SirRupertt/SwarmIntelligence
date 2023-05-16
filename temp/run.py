import random
from mpl_toolkits import mplot3d
from swarm import Swarm
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import numpy as np

# Define fitness function
def fitness_func(position):
    #x = position[0]
    #(x+3)(x-2)^2(x+1)^3
    #return ((x+3)((x-2)**2)((x+1)**3))
    return (position[0] **2 + position[1] **2)/5

# Set up the swarm
num_particles = 50
dim = 2
bounds = [[-5, 5], [-5,5]]
swarm = Swarm(num_particles, dim, bounds, fitness_func)
# Optimize the function
max_iter = 30
swarm.optimize(max_iter)
arrGen = swarm.getHistory()

# Print the best solution found
print("Best position:", swarm.global_best_position)
print("Best fitness:", swarm.global_best_fitness)

fig = plt.figure()
ax = plt.axes(projection='3d')
#plt.xlim([-15,15])
#plt.ylim([0, 100])

x = np.linspace(-6,6,25)
y = np.linspace(-6,6,25)

X, Y = np.meshgrid(x, y)
Z = fitness_func([X, Y])

#ax.contour3D(X, Y, Z, 50, cmap='binary')

counter = 0
#Each Gen List 
for epoch in arrGen:
    # plot the swarm at that epoch
    # save as a png
    #Each particle arr in the generation 
    ax = plt.axes(projection='3d')
    for particle in epoch:
        ax.contour3D(X, Y, Z, 35, cmap='binary', linewidths=0.75)
        ax.scatter3D(particle[0], particle[1], fitness_func(particle))
        ax.view_init(elev=10., azim=-15)
        #plt.figtext(0, .9, "Generation: " + str(counter), fontsize=15)
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

print("GIF COMPLETE.")
