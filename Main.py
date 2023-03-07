import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random
from Agent import Agent

fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

agents = []
def init():
    for i in range(10):
        N = 5
        agents.append(Agent((random.randint(0,N)*100), (random.randint(0,N)*100), (random.randint(-N,N)*5), (random.randint(-N,N)*5)))


def update(i):
    ax.clear()
    for i in range(0,len(agents)):
        agents[i].Update()
        ax.scatter(agents[i].getPos()[0], agents[i].getPos()[1], 50, marker='x')
        plt.quiver(agents[i].getPos()[0], agents[i].getPos()[1], agents[i].getVel()[0], agents[i].getVel()[1])


init()
ani = animation.FuncAnimation(fig=fig, func=update, frames=30, interval=100)
ani.save('Scatter.gif', writer='pillow')
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Swarm Intelligence")  # Add a title to the axes.