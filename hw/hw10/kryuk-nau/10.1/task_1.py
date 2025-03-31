# Базовий клас Polygon
class Polygon:
    def __init__(self, sides):
        self.sides = sides  # Список сторін полігону

    def perimeter(self):
        """Метод для обчислення периметра полігону"""
        return sum(self.sides)

# Клас Rectangle, що наслідує від Polygon
class Rectangle(Polygon):
    def __init__(self, width, height):
        # Для прямокутника кількість сторін 4, і дві сторони рівні ширині, а інші дві - висоті
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        """Метод для обчислення площі прямокутника"""
        return self.width * self.height


# Приклад використання:
# Створимо прямокутник з шириною 5 і висотою 10
rectangle = Rectangle(3, 30)

# Обчислимо площу
print(f"Area of rectangle: {rectangle.area()}")  # Виведе: 50

# Обчислимо периметр (використовуючи метод з базового класу)
print(f"Perimeter of rectangle: {rectangle.perimeter()}")  # Виведе: 30
