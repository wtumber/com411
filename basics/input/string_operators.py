def run():
    print("Please enter the number of lives.")
    lives = int(input())

    print("Please enter the energy level.")
    nrg = int(input())

    print("Please enter the shield level.")
    shields = int(input())

    print("Health has been set.")

    print("Lives: {}".format("<3 "*lives))
    print("Energy: {}".format("*"*nrg))
    print("Shield: {}".format("*"*shields))