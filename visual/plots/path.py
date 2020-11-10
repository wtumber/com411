import matplotlib.pyplot as plt

def coordinate():
    print("give me an x and y")
    x_value = int(input())
    y_value = int(input())
    return (x_value,y_value)

def path():
    print("retrieving path")
    x_values = []
    y_values = []
    counter = 0
    while counter < 4:
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
        counter = counter + 1
    return [x_values, y_values]

def run():
    values = path()
    plt.plot(values[0],values[1],"ro--")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()

run()