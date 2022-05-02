product = 1
n = int(input("Enter the number of real numbers: "))
for i in range(n):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)