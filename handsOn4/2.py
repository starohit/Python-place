# calculate area of a circle,volume of cylinder,volume of cone by taking required to be input from user.

import math


def area(rad):
    print(math.pi*rad*rad)


def vol1(rad, hei):
    return math.pi * rad * rad * hei


def vol2(rad, hei):
    return math.pi * rad * rad * hei * (1 / 3)


choice = int(input("enter choice: \n 1:area of circle \n 2:volume of cylinder \n 3:volume of cone \n"))
if choice == 1:
    r = int(input("enter the Radius "))
    area(r)
elif choice == 2:
    r = int(input("enter the Radius "))
    h = int(input("enter height of cylinder "))
    print(vol1(r, h))
elif choice == 3:
    r = int(input("enter the Radius "))
    h = int(input("enter height of cone "))
    print(vol2(r, h))
else:
    print("invalid input ")
