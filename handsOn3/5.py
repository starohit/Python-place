# register new user and can log in existing user using dictionary

database = {'Rohit': '1234', 'Raj': '5678', 'Ravi': '9012'}

name = input('Enter username: ')
if name in database:
    pin = input('Enter pin: ')
    if pin in database[name]:
        print('Welcome', name)
    else:
        print("You're logged in")
else:
    print("you are new , to register enter your name: ")
    n1 = input("create a name: ")
    p1 = input("create pin: ")
    d1 = {n1: p1}
    database.update(d1)
    print("congrats you're registered! ")

print(database)
