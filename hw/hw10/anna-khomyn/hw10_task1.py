class Polygon:
    def __init__(self, *arg):
        print(f"Polygon initialization...")

    def square(self):
        print("Counting polygon square...")


class Rectangle(Polygon):
    def __init__(self, length, width):
        print(f"Rectangle initialization: length = {length}, width = {width}")
        self.length = length
        self.width = width

    def square(self):
        print("Counting rectangle square:")
        return self.length * self.width

if __name__ == '__main__':

    p = Polygon()
    p.square()

    r = Rectangle(5, 4)
    print(r.square())