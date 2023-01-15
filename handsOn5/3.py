# Calculate area of Square, Rectangle and triangle by using same function “area()” .

# function Overloading

import math


class Square:
    def area(self, s):
        print("Area of Square: ", s * s)


class Rectangle:
    def area(self, b, h):
        print("Area of Rectangle: ", b * h)


class Triangle:
    def area(self, b, h):
        print("Area of triangle: ", 0.5 * b * h)


t1 = Triangle()
t1.area(6, 3)

r1 = Rectangle()
r1.area(4, 4)

s1 = Square()
s1.area(7)