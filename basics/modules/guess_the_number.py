import random

def guess_the_number():
    print("Please enter the minimum value:")
    min_val = int(input())
    print("Please enter the maximum value:")
    max_val = int(input())
    rand_between = random.randrange(min_val,max_val,1)
    guess_val = 1
    print("I am thinking of a number between {} and {}.  Can you guess what it is?".format(min_val,max_val))
    while guess_val != rand_between:
        guess_val = int(input())
        if guess_val < rand_between:
            print("too low")
        elif guess_val > rand_between:
            print("too high")
        else:
            pass
    print("Guessed correctly")

guess_the_number()
