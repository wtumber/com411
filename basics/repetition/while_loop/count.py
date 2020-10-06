print("how many should I avoid?")
to_avoid = int(input())

avoided_cables = 0
print()

while (avoided_cables < to_avoid):
    print("Avoiding", end="")
    avoided_cables += 1
    print("{} cables avoided.".format(avoided_cables))