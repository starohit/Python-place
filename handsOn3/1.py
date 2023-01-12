# calculator

n1 = int(input("What's the first number? "))
operation = str(input("Pick an operation: \n + \n - \n * \n / \n "))
n2 = int(input("What's the next number?: \n"))
d1 = {"+": n1+n2, "-": n1-n2, "*": n1*n2, "/": n1/n2}

if operation in d1:
    print(d1[operation])
else:
    print("Invalid operator")

