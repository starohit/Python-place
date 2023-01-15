# Overload * operator using Operator Overloading

class Product:
    def __init__(self, a):
        self.a = a

    def __mul__(self, other):
        return self.a * other.a


s1 = Product(5)
s2 = Product("hey")
print(s1 * s2)
