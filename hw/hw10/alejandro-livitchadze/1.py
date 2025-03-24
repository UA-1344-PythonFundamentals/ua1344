class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    def square(self):
        return self.width * self.height
    
    
rectangle = Rectangle(10, 20)
print(rectangle.square())

