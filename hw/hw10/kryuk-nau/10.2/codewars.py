# Regular Ball Super Ball

class Ball:
    def __init__(self, ball_type="regular"):
        # Приймаємо аргумент для ball_type з дефолтним значенням "regular"
        self.ballType = ball_type

# Приклад використання:

# Створення об'єкта без аргументів (тип м'яча буде "regular")
ball1 = Ball()
print(ball1.ballType)  # Виведе: regular

# Створення об'єкта з аргументом (тип м'яча буде "super")
ball2 = Ball("super")
print(ball2.ballType)  # Виведе: super



# Color Ghost

import random

class Ghost:
    def __init__(self):
        # Випадковий вибір кольору з доступних варіантів
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Приклад використання:

# Створення об'єкта класу Ghost
ghost = Ghost()

# Виведення кольору об'єкта
print(ghost.color)  # Виведе: "white", "yellow", "purple" або "red"


# Basic subclasses - Adam and Eve

# Базовий клас для обох
class Human:
    def __init__(self, name):
        self.name = name

# Клас Man, який успадковується від Human
class Man(Human):
    def __init__(self):
        super().__init__("Adam")  # Адам - перший чоловік

# Клас Woman, який успадковується від Human
class Woman(Human):
    def __init__(self):
        super().__init__("Eve")  # Єва - перша жінка

# Функція creation, яка створює масив з Адама та Єви
def creation():
    return [Man(), Woman()]

# Приклад використання:

# Створення Адама та Єви
adam_and_eve = creation()

# Виведення імен Адама та Єви
print(adam_and_eve[0].name)  # Виведе: Adam
print(adam_and_eve[1].name)  # Виведе: Eve


# Classy Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def getInfo(self):
        return f"{self.name}s age is {self.age}"

if __name__ == "__main__":
    person = Person("john", 34)
    print(person.getInfo)


# Building Spheres

import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        density = self.mass / volume
        return round(density, 5)

if __name__ == "__main__":
    ball = Sphere(3, 33)
    print(ball.get_radius())
    print(ball.get_mass())
    print(ball.get_volume())
    print(ball.get_surface_area())
    print(ball.get_density())

    
# Python's Dynamic Classes #1

def change_class_name(cls, new_name):
    if not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter")
    if not new_name.isalnum():
        raise ValueError("Class name must contain only alphanumeric characters")
    
    cls.__name__ = new_name
    return cls

class MyClass:
    pass

# Test cases
if __name__ == "__main__":
    # Valid renaming
    MyClass = change_class_name(MyClass, "UsefulClass")
    print(MyClass.__name__)  # Outputs: UsefulClass

    MyClass = change_class_name(MyClass, "SecondUsefulClass")
    print(MyClass.__name__)

    try:
        change_class_name(MyClass, "usefulClass")
    except ValueError as e:
        print(e)

    try:
        change_class_name(MyClass, "Useful_Class")
    except ValueError as e:
        print(e)