import matplotlib.pyplot as plt
def small():
    plt.plot([3,4,4,3,3],[3,3,4,4,3],'ro:')
    

def medium():
    plt.plot([2,5,5,2,2],[2,2,5,5,2],'gs--')
    

def large():
    plt.plot([1,6,6,1,1],[1,1,6,6,1],'bx-')
    

small()
medium()
large()
plt.show()