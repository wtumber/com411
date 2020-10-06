print("Where should I look?")
place = input()

# Check the bedroom
if (place == "in the bedroom"):
    print("Where in the bedroom?")
    bedroom = input()

    if (bedroom == "under the bed"):
        print("Found shoes but no battery")
    else:
        print("Found mess but no battery") 

# Check the bathroom
elif (place == "in the bathroom"):
    print("Where in the bathroom?")
    bathroom = input()

    if (bathroom == "in the bathtub"):
        print("rubber duck but no battery")
    else:
        print("wet surface but no battery")

elif (place == "in the lab"):
    print("Where in the lab?")
    lab = input()

    if (lab == "on the table"):
        print("Found battery")
    else:
        print("tools but no battery")

else:
    print("Unknown place.")