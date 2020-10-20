def likelihood():
    likelihood_fall = ()
    likelihood_fall = likelihood_fall + (50, 38, 27, 99, 4)
    print("Minimum Likelihood of falling: {}%".format(min(likelihood_fall)))
    print("Maximum Likelihood of falling: {}%".format(max(likelihood_fall)))

likelihood()