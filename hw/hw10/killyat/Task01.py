class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"Rectangle square: {rect.square()}")