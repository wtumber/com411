def run():
    print("What type of adventure:Scary, short, safe, long")
    advent_type = input()

    if advent_type == "scary" or advent_type == "short":
        print("Dark forest then")
    elif advent_type == "long" or advent_type == "safe":
        print("Safe route then")
    else:
        print("wrong entry")
