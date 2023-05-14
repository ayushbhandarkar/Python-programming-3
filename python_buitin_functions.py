# wap to implement built-in functions of class

class Student:
    name = ""
    id = 0
    age = 0

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


s = Student("John", 101, 22)

# this function prints the value of attribute of the object s
print(" Age : ", getattr(s, 'age'))

# reset the value of attribute age to 23
setattr(s, "age", 23)
print(" Age : ", s.age)    # prints the modified value of age
# print(" after changing Age : ", getattr(s, "age"))

# prints true if the student contains the attribute with name gender
print(" Attribute available : ", hasattr(s, 'id'))

# deletes the attribute age
delattr(s, 'age')
print(" Age : ", s.age)
