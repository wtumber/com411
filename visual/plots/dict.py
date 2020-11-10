import matplotlib.pyplot as plt

def data():
    path = {}
    print("What type of line:\n--\n-\n:")
    path["linestyle"] = input()
    print("Colour:\nr\ng\nb")
    path["colour"] = input()
    print("shape:\no\ns\n^\nv\nx")
    path["shape"] = input()
    return path

def generate():
    print("How many lines would you like to display")
    lines = int(input())
    for line in range(lines):
        linestyle = data()
        linestyle_vals = "".join(list(linestyle.values()))
        plt.plot([0,line+1],[line+1,line+2],linestyle_vals)
    plt.show()

def run():
    print("Running")
    generate()
    print("Done")

run()