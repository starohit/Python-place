# check if the 2nd set is subset of 1st set and if it is subset find the difference of both set

a = {2, 3, 5, 34, 7, 23, 6, 42, 43, 12, 11}
b = {3, 5, 34, 7, 23, 6, 42}

if a.issubset(b):
    print(a-b)
else:
    print("not a subset")
