#  constructor overloading 

class sample:
    a = 10
    def __init__(self):
        print(" First constructor with : ")

    def __init__(self):
        print(" Second constructor ")


obj = sample()
print(obj.a)
