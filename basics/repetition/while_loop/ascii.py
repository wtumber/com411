def run():
    print("how many bars should be charged")
    bars_to_charge = int(input())

    bars_charged = 0
    print()

    while bars_charged < bars_to_charge:
        bars_charged += 1
        print("charging: {}".format("█" * bars_charged))

    print("battery fully charged")