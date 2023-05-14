class Base1:
    def showbase(self):
        print(" Function of base class called")


class derive1(Base1):

    def show_derive1(self):
        print(" Function of first derive class ")


class Base2:
    def showbase2(self):
        print(" Function of second derive class ")


class derive2(Base1, Base2):
    def show_derive2(self):
        print(" Function of second derive class")


class derive3(derive1, derive2):
    def show_derive3(self):
        print(" Function of third derive class ")


obj = derive3()
obj.showbase()
obj.showbase2()
obj.show_derive1()
obj.show_derive2()
obj.show_derive3()
