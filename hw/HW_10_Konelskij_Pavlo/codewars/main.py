#1 Ball-super-ball

class Ball(object):
    # your code goes here
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"    

#2 Color-ghost
import random

class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

#3 Basic-subclasses-Adam-and-Eve
class Human:
    def __init__(self):
        self.species = "Homosapienc"

class Man(Human):
    def __init__(self):
        super().__init__()
        self.gender = "Male"

class Woman(Human):
    def __init__(self):
        super().__init__()
        self.gender = "Female"

def God():
    return [Man(), Woman()]

#4 Classy-classes
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    
#Building Spheres
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

#Dynamic Classes
import re

def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        cls.__name__ = new_name
    else:
        raise ValueError
    