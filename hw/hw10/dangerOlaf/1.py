# Task 1
# Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    def __init__(self, pol_side):
        self.pol_side = pol_side

class Rectangle(Polygon):
    
    def __init__(self, a, b):
        super().__init__(4)
        self.a = a
        self.b = b
    
    def square(self):
        return self.a * self.b
    
rect = Rectangle(5,10)
print(rect.square())