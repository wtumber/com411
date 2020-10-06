print("num1")
num1= int(input())
print("num2")
num2= int(input())
print("num3")
num3= int(input())

even_count = 0
odd_count  = 0

if num1 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if num2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1    

if num3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print("{} even and {} odd".format(even_count,odd_count))   