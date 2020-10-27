def observed():
    observations = []
    while len(observations)<5:
        print("Input a place:")
        observations.append(input())
    return observations

def remove_observations(obs_list):
    print("Do you wish to remove observations?\nyes\nno")
    yesno = input()
    while yesno == "yes":
        print("Enter string of place to remove")
        remove = input()
        obs_list.remove(remove)
        print("Done!")
        print("Do you wish to remove observations?\nyes\nno")
        yesno = input()
    return obs_list

def run():
    original_list = observed()
    obs = remove_observations(original_list)
    obs_count = set()
    for place in obs:
        place_count = obs.count(place)
        obs_count.add((place,place_count))
    print(obs_count)
    for tup in obs_count:
        print("{} observed {} times".format(tup[0],tup[1]))

run()











