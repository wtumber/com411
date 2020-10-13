def cross_bridge(steps):
    for step in range(steps+1):
        print("Crossed Step")

    if steps <= 5:
        print("We must keep going")
    else:
        print("Bridge is collapsing")

cross_bridge(3)
cross_bridge(6)