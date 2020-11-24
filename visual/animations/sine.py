import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

#y = np.sine(x_in_radians)

fig, ax = plt.subplots()
def animate(frame):
    ax.set_xlim(0,720)
    ax.set_ylim(-1,1)
    x = np.arange(0,frame,1)
    y = np.sin((np.pi/180)*x)
    ax.plot(x,y,"r")

def run():
    simple_animation = animation.FuncAnimation(fig,animate, 
                            frames=720,interval=100)
    plt.show()

run()
