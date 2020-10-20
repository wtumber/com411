def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction")
    direction_list = directions()
    for index in range(len(direction_list)):
        print("{} :{}".format(index,position[index])

def run():
    return menu()

run()