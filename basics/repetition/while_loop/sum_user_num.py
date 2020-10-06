print("How many num should i add")
number_to_add = int(input())

# Declare a control variable
added = 0

# Display blank line
print()

# Sum numbers
total = 0

while (added < number_to_add):
    print("Please enter number {} of {}:".format(added number_to_add)
    number = int(input())
    total += number
    added = added + 1

# Display result
print("The answer is", total)