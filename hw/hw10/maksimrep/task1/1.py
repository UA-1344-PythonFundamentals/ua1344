#Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of the rectangle.

class Многоугольник:
    def __init__(self, количество_сторон):
        self.количество_сторон = количество_сторон

    def __str__(self):
        return f"Многоугольник с {self.количество_сторон} сторонами"


class Прямоугольник(Многоугольник):
    def __init__(self, длина, ширина):
        super().__init__(4)  # All time 4 side
        self.длина = длина
        self.ширина = ширина

    def площадь(self):
        return self.длина * self.ширина

    def __str__(self):
        return f"Прямоугольник с длиной {self.длина} и шириной {self.ширина}, площадь: {self.площадь()}"


прямоугольник = Прямоугольник(5, 3)
print(прямоугольник)
