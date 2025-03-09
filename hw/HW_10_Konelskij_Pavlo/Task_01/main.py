class Polygon:
    def __init__(self,sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(12,16)

print(f"Rectangle area: {rect.area()}")