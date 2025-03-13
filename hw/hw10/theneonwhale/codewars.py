# 1. Ball super ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

print("--------------------------------------")
print("Task 1. Ball super ball")
ball = Ball()
print(f"ball type: {ball.ball_type}")
ball2 = Ball("irregular")
print(f"ball type: {ball2.ball_type}")
print("--------------------------------------")

# 2. Color Ghost
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

print("Task 2. Color Ghost")
ghost = Ghost()
print(f"ghost color: {ghost.color}")
print("--------------------------------------")

# 3. Basic subclasses - Adam and Eve
class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello, I am {self.name}."


class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)
        self.gender = "Male"

    def __str__(self):
        return f"Hello, I am {self.name}, a man."


class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)
        self.gender = "Female"

    def __str__(self):
        return f"Hello, I am {self.name}, a woman."


def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


print("Task 3. Basic subclasses - Adam and Eve")
humans = God()
for human in humans:
    print(human)
print("--------------------------------------")

# 4. Classy Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

    def get_info(self):
        return f"{self.name}s age is {self.age}"

print("Task 4. Classy Classes")
john = Person("John", 34)
print(john.info)
print(john.get_info())
print("--------------------------------------")

# 5. Building Spheres
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
        volume = (4/3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        volume = self.get_volume()
        density = self.mass / volume
        return round(density, 5)

print("Task 5. Building Spheres")
ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())
print("--------------------------------------")

# 6. Python's Dynamic Classes
def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ValueError("Class name must be alphanumeric and start with an uppercase letter.")

print("Task 6. Python's Dynamic Classes")
class MyClass:
    pass

try:
    print(f"Original class name: {MyClass.__name__}")
    class_name_changer(MyClass, "UsefulClass")
    print(f"Changed class name: {MyClass.__name__}")

    class_name_changer(MyClass, "secondUsefulClass")
except ValueError as e:
    print(e)
print("--------------------------------------")
