import matplotlib as mpl
import matplotlib.pyplot as plt
#import numpy as np
import matplotlib.animation as animation
#import random
from Agent import Agent
import Swarm

fig, ax = plt.subplots()  # Create a figure containing a single axes.\\\
Swarm = Swarm.Swarm()
print(Swarm.getSwarm())

def update():
    ax.clear()
    agents = Swarm.getSwarm()
    for i in range(0,len(agents)):
        Swarm.update()
        ax.scatter(agents[i].getPos()[0], agents[i].getPos()[1], 50, marker='x')
        plt.quiver(agents[i].getPos()[0], agents[i].getPos()[1], agents[i].getVel()[0], agents[i].getVel()[1])


ani = animation.FuncAnimation(fig=fig, func=update, frames=30, interval=100)
ani.save('Scatter.gif', writer='pillow')
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Swarm Intelligence")  # Add a title to the axes.