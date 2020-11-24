import csv
import matplotlib.pyplot as plt

##incomplete function
##
##
def read_data():
    with open("C:/Users/ISA06006086/Documents/University/com411/visual/subplots/train.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile,delimiter=",")
        header = next(csv_reader)
        data = {}
        for row in csv_reader:
            pass

    return mydict 

read_data()