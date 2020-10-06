number = int(input())

count = 0 
total = 1

while count < number:
    count += 1
    total = total*count

print("factorial is {}".format(total))