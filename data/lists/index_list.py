def movements():
    path = []
    path.append("Move Forward")
    path.append(10)
    path.append("Move Backward")
    path.append(5)
    path.append("Move Left")
    path.append(3)
    path.append("Move Right")
    path.append(1)
    return path

def run():
    print("Moving...")
    path = movements()
    print("{} for {} steps".format(path[0],path[1]))
    print("{} for {} steps".format(path[2],path[3]))
    print("{} for {} steps".format(path[4],path[5]))
    print("{} for {} steps".format(path[6],path[7]))

run()