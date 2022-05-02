from itertools import count


n = int(input("Number of integers"))
sum = 0

for i in range(n):
    x = int(input("enter an integer"))
    sum = sum + x
avg = sum/n
print(" The avg is : ", avg)
