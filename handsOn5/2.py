# Create Three class “Space”, “Galaxy” and “Earth” and print variables of Space
# and Galaxy class in Earth class.


class Space:
    name = "Universe"


class Galaxy:
    g_name = "Milky Way"


class Earth(Space, Galaxy):
    type = "Planet"

    def show(self):
        print("In the vast", self.name)
        print("Earth is a", self.type)
        print("It is in the", self.g_name, "galaxy")


e1 = Earth()
e1.show()
