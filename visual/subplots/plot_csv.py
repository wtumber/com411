import csv
import matplotlib.pyplot as plt
def read_data():
    with open("C:/Users/ISA06006086/Documents/University/com411/visual/subplots/temps.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=" ")
        mydict = {}
        for row in csv_reader:
            for column, value in row.items():
                mydict.setdefault(column, []).append(float(value))
        print(mydict)
    return mydict 
    
def run():
    data = read_data()
    fig, axes = plt.subplots(2,1,sharex="all")
    axes[0].plot(data["week1"])
    axes[1].plot(data["week2"])
    plt.show()

run()


