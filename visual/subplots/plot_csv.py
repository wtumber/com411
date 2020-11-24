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


#model answer for reading in csv from prins
def read_data_model_answer():
    with open("") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)
        data = {header[0].strip():[],
                header[1].strip():[]}
        for row in csv_reader:
            data[header[0]].append(row[0].strip())
            data[header[1]].append(row[1].strip())
        return data





