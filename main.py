class Disha:
    course = ""
    duration = 0

    def input(self, course, duration):
        self.course = course
        self.duration = duration

    def display(self):
        print("Course name : ", self.course)
        print("Duration of course : ", self.duration)


khushi = Disha()
khushi.input("python", 5)
khushi.display()
del khushi
try:
    khushi.display()
except:
    print(" Object has been deleted")