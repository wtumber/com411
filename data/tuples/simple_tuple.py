def likelihood():
    likelihood = (50, 38, 27, 99, 4)
    return min(likelihood)

def run():
    min_likelihood = likelihood()
    print("Minimum likelihood of falling: {}%".format(min_likelihood))