# Regular Ball Super Ball
class Ball(object):
    def __init__(self, type = "regular"):
        self.ball_type = type
        
# Color Ghost
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
        
# Basic subclasses Adam and Eve
def God():
    return [Man(), Woman()]

    
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

# Classy Classes
class Person:
    def __init__(self, name, age):
        self.info= f"{name}s age is {age}"
        
# Building Spheres
from math import pi, pow

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4 / 3 * pi * pow(self.radius, 3), 5)
    
    def get_surface_area(self):
        return round(4 * pi * pow(self.radius, 2), 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    
# Python's Dynamic Classes #1
import re
def class_name_changer(cls, new_name):
    if not re.fullmatch(r"[A-Z][a-zA-Z0-9]*", new_name):
        raise ValueError("Invalid class name")
    cls.__name__ = new_name