def observed():
    observations = []
    while len(observations)<5:
        print("Input a place:")
        observations.append(input())
    return observations

def run():
    print("Counting observations...")
    obs = observed()
    obs_count = set()
    for place in obs:
        place_count = obs.count(place)
        obs_count.add((place,place_count))
    print(obs_count)
    for tup in obs_count:
        print("{} observed {} times".format(tup[0],tup[1]))

run()