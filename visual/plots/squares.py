import matplotlib.pyplot as plt
def small():
    plt.plot(x=[3,4,4,3],y=[3,3,4,4],'ro:')
    plt.show()

def medium():
    plt.plot(x=[2,5,5,2],y=[2,2,5,5],'gs--')
    plt.show()

def large():
    plt.plot(x=[1,6,6,1],y=[1,1,6,6],'bx')
    plt.show()

small()
medium()
large()