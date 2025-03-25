class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides

class Rectangle(Polygon):
        def __init__(self, width, height):
            super().__init__(4)
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

rectangle = Rectangle(2,4)
print(f"Rectangle area = {rectangle.area()}")