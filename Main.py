import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Swarm

fig, ax = plt.subplots()  # Create a figure containing a single axes.\\\
Swarm = Swarm.Swarm()

def update():
    ax.clear()
    for i in Swarm.getSwarm():
        Swarm.update()
        ax.scatter(i.getPos()[0], i.getPos()[1], 50, marker='x')
        plt.quiver(i.getPos()[0], i.getPos()[1], i.getVel()[0], i.getVel()[1])

update()
plt.show()

ani = animation.FuncAnimation(fig=fig, func=update, frames=30, interval=100)
ani.save('Scatter.gif', writer='pillow')
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Swarm Intelligence")  # Add a title to the axes.