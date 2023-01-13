# Compare time of execution between factorial of 899 with and without function recursion.
import time

# Recursion

begin = time.time()


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = 899

print("Factorial of", num, "is",
      factorial(num))
end = time.time()
print(round(end-begin, 6))

# Iteration
begin2 = time.time()


def fac(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


num = 899

print("Factorial of", num, "is",
      fac(num))
end2 = time.time()
print(round(end2-begin2, 6))
