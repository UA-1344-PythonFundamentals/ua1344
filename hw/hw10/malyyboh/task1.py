class Polygon:
    def __init__(self, **sides: dict):
        self.sides = dict(sides)


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(width=width, height=height)

    def output_sides_rectangle(self):
        for k, v in self.sides.items():
            print(f"{k}: {v}")

    def square_rectangle(self):
        square = self.sides["width"] * self.sides["height"]
        print(f"The square of the rectangle is {square}")


rect = Rectangle(4, 5)
rect.output_sides_rectangle()
rect.square_rectangle()
