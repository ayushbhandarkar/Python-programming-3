# multilevel inheritance

class Base:

    def display_base(self):
        print(" This function belongs to base class")


class Derive1(Base):

    def display_derive1(self):
        print("This function belongs to derive class 1 ")


class Derive2(Derive1):

    def display_derive2(self):
        print(" This function belongs to derive class 2")


class Derive3(Derive2):

    def display_derive3(self):
        print(" This function belongs to derive class 3")


obj = Derive3()
obj.display_base()
obj.display_derive1()
obj.display_derive2()
obj.display_derive3()
