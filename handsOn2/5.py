l1 = list(range(1, 101))

odd = [i for i in l1 if i % 2 != 0]
even = [i for i in l1 if i % 2 == 0]

print("odd numbers are : ", odd)
print("even number are : ", even)
