class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
class Rectangle(Polygon):
    def area(self):
        return self.length * self.width

rect = Rectangle(2, 40)
print("Area of Rectangle:", rect.area())
