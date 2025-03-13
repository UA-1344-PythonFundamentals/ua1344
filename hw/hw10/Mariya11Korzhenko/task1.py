class Polygon():
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, height, weight):
        super().__init__(4)
        self.height = height
        self.weight = weight

    def area(self):
        return self.height * self.weight

triangle = Rectangle(3, 4)
print(triangle.area())


