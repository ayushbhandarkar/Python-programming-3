class Person:
    age = 0
    name = ""

    def __init__(self, nm, a):      # parameterized constructor
        self.age = a
        self.name = nm

    def display(self):
        print(" Name : ", self.name)
        print(" Age : ", self.age)


obj = Person("Rohan", 20)
obj.display()
