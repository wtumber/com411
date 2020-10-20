def steps():
    likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),
    ("step 4", 99),
    ("step 5", 4)]
    return likelihoods

def run():
    likelihoods = steps()
    good_steps = []
    bad_steps =[]
    for item in likelihoods:
        if item[1] < 50:
            good_steps.append(item)
        else:
            bad_steps.append(item)
    print("Good steps: {} \nBad steps: {}".format(len(good_steps),len(bad_steps)))
