class Student:
    name = "Abc"
    rollno = 101

    def display(self):
        print("Name : ", self.name)
        print("Roll no. : ", self.rollno)


obj = Student()
# print("data of datamember using getattr() : ", getattr(obj, "name"))

# setattr(obj, "name", "XYZ")
# print(" Replaced data of Name : ", obj.name)

# result = hasattr(obj, "age")
# print(result)

delattr(obj, "rollno")

try:
    print(" Rollno : ", obj.rollno)
except AttributeError:
    print(" The attribute has been deleted")
