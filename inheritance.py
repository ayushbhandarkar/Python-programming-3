# wap to implement single inheritance

class Base:
    def function1(self):
        print(" This is the function of old / base class ")


class Derive(Base):
    def function2(self):
        print(" This is the function of Second / derive class ")


obj1 = Base()
obj1.function1()

obj2 = Derive()
obj2.function2()
