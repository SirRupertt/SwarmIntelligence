import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
points = []
vels = []
def init():
    for i in range(10):
        N = 5
        x = random.randint(0,N)*100
        y = random.randint(0,N)*100
        points.append([x,y])
        velx = random.randint(-N,N)*5
        vely = random.randint(-N,N)*5
        vels.append([velx, vely])


def update(i):
    ax.clear()
    for i in range(0,len(points)):
        N = 5
        points[i][0]+=vels[i][0]
        points[i][1]+=vels[i][1]
        vels[i][0] = random.randint(-N,N)*5
        vels[i][1] = random.randint(-N,N)*5
        ax.scatter(points[i][0], points[i][1], 50, marker='x')
        plt.quiver(points[i][0],points[i][1], vels[i][0], vels[i][1])


init()
ani = animation.FuncAnimation(fig=fig, func=update, frames=30, interval=100)
ani.save('Scatter.gif', writer='pillow')
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Swarm Intelligence")  # Add a title to the axes.

plt.show()