class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def get_info(self):
        return f"Це багатокутник з {self.num_sides} сторонами."

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def get_info(self):
        return f"Прямокутник зі сторонами {self.width} та {self.height} та площею {self.area()}."

# rectangle = Rectangle(12, 10)
# print(rectangle.get_info())
# print(rectangle.area())