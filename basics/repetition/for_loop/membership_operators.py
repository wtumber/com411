print("What phrase do you see?")
phrase = input()

print("The phrase reversed is", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed) 