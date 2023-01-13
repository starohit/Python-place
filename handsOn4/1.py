# guess game

import random

target = random.randint(1, 100)
retries = 0
while True:
    choice = int(input("Enter your choice: "))
    retries += 1
    if target != choice:
        print("Wrong Guess!! Try Again")
        if target < choice:
            print("The required number lies between 0 and {}".format(choice))
        else:
            print("The required number lies between {} and 100".format(choice))
    else:
        print("You guessed the correct number after {} retries".format(retries))
        break
