class Area:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Area):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area_sqr(self):
        return self.length * self.width


class Cube(Area):
    def __init__(self,  length, width, height):
        super().__init__(length, width)
        self.height = height

    def area_cube(self):
        return self.length * self.width * self.height


square = Square(3, 4)
print("Area of square : ", square.area_sqr())

cube = Cube(3, 4, 2)
print("Area of Cube : ", cube.area_cube())
