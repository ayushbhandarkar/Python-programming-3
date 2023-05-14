# wap to implement constructor

class Sample:

    def __init__(self):         # properties of constructor using init
        print("Special member function of class is called")
    
    def local_function(self):
        print(" Local Function of class is called")


obj = Sample()      # obj-object     Sample - constructor
obj.local_function()
