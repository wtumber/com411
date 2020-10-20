def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("please select a direction")
    direction_list = directions()
    for index in range(len(direction_list)):
        print("{} :{}".format(index,direction_list[index]))
    chosen = int(input())
    return chosen


def run():
    route = []
    print("Working out escape method...")
    counter = 0
    direction_list = directions()
    while counter < 5 :
        counter += 1
        chosen = menu()
        route.append(direction_list[chosen])
    print("Escape route: {}".format(route))

