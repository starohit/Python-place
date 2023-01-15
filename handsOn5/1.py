# Create an “Animal” class and specify its attributes, then inherit the class
# “Tiger” and specify its special Attributes

class Animal:
    def __init__(self, food, water):
        self.eats = food
        self.drinks = water

    def habits(self):
        print("This Animal eats", self.eats, "and drinks", self.drinks)


class Tiger(Animal):
    def __init__(self, food, water, sound):
        super().__init__(food, water)
        self.voice = sound

    def speaks(self):
        print("This animal", self.voice)


x = Tiger("Meat", "Blood", "ROAR!!")
x.habits()
x.speaks()
