class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def create():
    return [Man(), Woman()]

people = create()

print(isinstance(people[0], Man))
print(isinstance(people[1], Woman))  
print(isinstance(people[0], Human))
print(isinstance(people[1], Human))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_info(self):
        return f"{self.name}s age is {self.age}"

person = Person("John", 34)
print(person.get_info)

person2 = Person("Alice", 25)
print(person2.get_info)


class Block:
    def __init__(self, dimensions):
        self.width, self.length, self.height = dimensions

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)

block = Block([3, 4, 5])
print(f"Width: {block.get_width()}")
print(f"Length: {block.get_length()}")
print(f"Height: {block.get_height()}")
print(f"Volume: {block.get_volume()}")
print(f"Surface Area: {block.get_surface_area()}")
    
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
        volume = self.get_volume()
        density = self.mass / volume
        return round(density, 5)

sphere = Sphere(3, 150)
print(f"Radius: {sphere.get_radius()}")
print(f"Mass: {sphere.get_mass()}")
print(f"Volume: {sphere.get_volume()}")
print(f"Surface Area: {sphere.get_surface_area()}")
print(f"Density: {sphere.get_density()}")


import re

def change_class_name(new_name):
    if re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        return new_name
    else:
        raise ValueError("Invalid class name. The name must start with an uppercase letter and contain only alphanumeric characters.")

try:
    class_name = change_class_name("SecondUsefulClass")
    print(f"Class name changed to: {class_name}")
except ValueError as e:
    print(e)