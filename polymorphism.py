class Animal:
    def speak(self):
        print("speaking")


class Dog(Animal):
    def speak(self):
        print("Barking")


a = Animal()
a.speak()

d = Dog()
d.speak()

