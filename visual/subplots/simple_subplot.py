import matplotlib.pyplot as plt
def read_data(file_path):
    with open(file_path) as file:
        file_info = []
        for line in file:
            file_info.append(float(line))
        file.close()
    return file_info

def run():
    data = read_data("C:/Users/ISA06006086/Documents/University/com411/visual/subplots/temps.txt")
    fig, axes = plt.subplots(1,2)
    axes[0].plot(data)
    axes[1].bar(data,data)
    plt.show()

run()



