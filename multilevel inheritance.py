# wap to implement multilevel inheritance

class Base1:
    def showBase1(self):
        print(" Function of base class is called ")


class derive1(Base1):
    def showDerive1(self):
        print(" Function of first Derive class is called ")


class derive2(derive1):
    def showDerive2(self):
        print(" Function of Second Derive class is called ")


obj = derive2()
obj.showDerive2()
obj.showDerive1()
obj.showBase1()
