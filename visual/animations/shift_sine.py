import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
    ax.cla()
    ax.set_xlim(-20,740)
    ax.set_ylim(-1.2,1.2)
    x = np.arange(0,720,1)
    y = np.sin((np.pi/180)*(x+frame))
    ax.plot(x,y,"r")

def run():
    simple_animation = animation.FuncAnimation(fig,animate, 
                            frames=720,interval=20)
    plt.show()

run()
