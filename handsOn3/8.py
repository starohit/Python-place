""" Create a tuple and if item of tuple are repeated make the item as key
and count as value and create a dictionary with that kay, value."""

t1 = ("apple", "mango", "banana", "cherry", "mango", "apple", "cherry", "apple", "cherry", "apple")

for x in t1:
    if t1.count(x) > 1:
        print(x, ':', t1.count(x))
    else:
        continue


