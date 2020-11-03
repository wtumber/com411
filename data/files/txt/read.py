def search(filename):
    print("Searching")
    with open(filename) as file:
        for line in file:
            print("Searching in {}".format(line))
    print("Done")

def run():
    search("locations.txt")

run()
