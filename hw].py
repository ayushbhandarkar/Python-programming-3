# single inheritance

class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person(self):
        print("Name :", self.name, "\nAge :", self.age)


class Employ(Person):
    Employ_id = 0
    Employ_salary = 0
    Employ_experience = 0

    def input(self):
        self.Employ_id = int(input(" Enter empolyee id : "))
        self.Employ_salary = int(input(" Enter empolyee salary : "))
        self.Employ_experience = int(input(" Enter Empolye Experience : "))

    def display(self):
        print("Employ id :", self.Employ_id, "\nEmploy salary:", self.Employ_salary, "\nEmploy experience : ",
              self.Employ_experience)


obj_emp = Employ("Disha", 20)
obj_emp.input()
obj_emp.person()
obj_emp.display()
