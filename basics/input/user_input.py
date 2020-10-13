def run():
    # Ask user to enter their name
    print("What is your name, human?")
    name = input()


    print("How old in years?")
    age = input()

    print("How tall are you in metres?")
    height = int(input())

    print("Weight in kg?")
    weight = int(input())

    #calculate bmi
    bmi = weight/(height**2)

    #print with 2dp format
    print("{0} you are {1} years old and your bmi is {2:.2f}".format(name, age,bmi))