class Person:
    name = ""
    age = 0

    def get_person(self, nm, a):
        self.name = nm
        self.age = a

    def show_person(self):
        print(" Name : ", self.name)
        print(" Age : ", self.age)


class student1(Person):
    course = ""
    grade = " "

    def showstudent1(self):
        course = input(" Enter your course name : ")
        grade = input(" Enter your grade : ")
