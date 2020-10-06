print("phrase?")
phrase = input()

print("\nReversing\nThe phrase is", end="")

for position in range(len(phrase) - 1, -1, -1): # step of -1, limit -1 ,length is phrase -1
    print(phrase[position], end="")