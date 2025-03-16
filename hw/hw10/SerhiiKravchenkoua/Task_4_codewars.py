# 1.

class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)  #=> "regular"
print(ball2.ball_type)  #=> "super"

# 2.

class Ghost:
    def __init__(self):
        import random
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost1 = Ghost()
ghost2 = Ghost()
ghost3 = Ghost()

print(ghost1.color)
print(ghost2.color)
print(ghost3.color)

#3.

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

class God():
    def __new__(cls):
        return [Man(), Woman()]

paradise = God()

print(isinstance(paradise[0], Man))
print(isinstance(paradise[1], Woman))
print(isinstance(paradise[0], Human))
print(isinstance(paradise[1], Human))

#4.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def info(self) -> str:
        return f"{self.name}s age is {self.age}"

    def get_info(self) -> str:
        return self.info

person = Person("Serhii", 39)
print(person.info)

#5.
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
        # Формула для об'єму кулі: (4/3) * π * r³
        volume = (4/3) * math.pi * self.radius ** 3
        return round(volume, 5)

    def get_surface_area(self):
        # Формула для площі поверхні кулі: 4 * π * r²
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)

    def get_density(self):
        # Обчислюємо густину без округлення об'єму
        volume = (4/3) * math.pi * self.radius ** 3
        density = self.mass / volume
        return round(density, 5)

ball = Sphere(2, 50)

print(ball.get_radius())          # 2
print(ball.get_mass())            # 50
print(ball.get_volume())          # 33.51032
print(ball.get_surface_area())    # 50.26548
print(ball.get_density())         # 1.49208

#6.

import re

def class_name_changer(cls, new_name):
    if not isinstance(new_name, str):
        raise ValueError("Class name must be a string.")

    if not re.fullmatch(r'[A-Z][a-zA-Z0-9]*', new_name):
        raise ValueError(
            "Invalid class name. It must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name

    return cls

class MyClass:
    pass

print(MyClass.__name__)
class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)
class_name_changer(MyClass, "SecondUsefulClass")
print(MyClass.__name__)