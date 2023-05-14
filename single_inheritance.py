class Person:
    name = ""
    age = 0

    def input(self):
        self.name = input(" Enter the name : ")
        self.age = input(" Enter the age : ")

    def output(self):
        print("Name ", self.name)
        print("Age : ", self.age)


class Student(Person):
    course = ""
    per = 0

    def get_details(self):
        self.course = input(" Enter the course : ")
        self.per = input(" Enter the perc   entage : ")

    def show_details(self):
        print(" Course name : ", self.course)
        print(" Percentage : ", self.per)


print("\t\t\t\t\t Details of person ")
obj1 = Person()
obj1.input()
obj1.output()


print("\t\t\t\t\t Details of student ")
obj2 = Student()
obj2.input()
obj2.get_details()
obj2.output()
obj2.show_details()
