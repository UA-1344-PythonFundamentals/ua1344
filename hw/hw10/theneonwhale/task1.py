class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        raise NotImplementedError("Subclasses should implement this method")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(5, 3)
print(f"Rectangle - Sides: {rectangle.sides}, Length: {rectangle.length}, Width: {rectangle.width}")
print(f"Area of Rectangle: {rectangle.area()}")
