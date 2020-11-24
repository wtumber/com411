import matplotlib.pyplot as plt
import matplotlib.animation as animation


data = []
fig, ax = plt.subplots()

def init():
    global data
    data.append({"x":[2,2,3,3,2],"y":[2,3,3,2,2]})
    data.append({"x":[1,1,4,4,1],"y":[1,4,4,1,1]})
    data.append({"x":[0,0,5,5,0],"y":[0,5,5,0,0]})

def animate(frame):
    global ax
    index = frame % len(data)
    ax.cla()
    ax.set_xlim(-1,6)
    ax.set_ylim(-1,6)
    ax.plot( data[index]["x"],data[index]["y"] ,"r")

def run():
    global fig
    simple_animation = animation.FuncAnimation(fig,animate, 
                            frames=4,interval=100,init_func=init())
    plt.show()

run()



