# ==========    1   ==========

class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

# ==========    2   ==========

import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

Casper = Ghost()
print(f"\n== 2 ==>> Hello, I'm {Casper=} and I am {Casper.color}")

# ==========    3   ==========

def God():
    return [Man("Adam"), Woman("Eve")]
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass

class Woman(Human):
    pass

first_humans = God()
print(f"\n== 3 ==>> The first humans are: {first_humans[0].name}, {first_humans[1].name}")

# ==========    4   ==========

class Person:
    def __init__(self, name, age):
        #self.info=f"#{name}s age is #{age}"
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    
p = Person("Mary", 25)
print(f"\n== 4 ==>> {p.info}")

# ==========    5   ==========

from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(pi * self.radius ** 3 * 4/3, 5)
    
    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    
ball = Sphere(2,50)
print("\n== 5 ==>>")
print(f"{ball.get_radius() = }")
print(f"{ball.get_mass() = }")
print(f"{ball.get_volume() = }")
print(f"{ball.get_surface_area() = }")
print(f"{ball.get_density() = }")

# ==========    6   ==========

import re

def class_name_changer(cls, new_name):
    ptrn = r'^[A-Z]+[A-Za-z0-9]*$'
    if re.match(ptrn, new_name):
        cls.__name__ = new_name
        return cls
    else:
        raise Exception ("Error")

class MyClass:
    pass


print("\n== 6 ==>>")
test = MyClass()

class_name_changer(MyClass, "MyUsefulClass")
print("MyUsefulClass: ", MyClass.__name__)

try:
    class_name_changer(MyClass, "myUsefulClass")
    print(MyClass.__name__)
except Exception as error:
    print("myUsefulClass: ", error)
try:
    class_name_changer(MyClass, "MyUsefulCl@ss")
    print(MyClass.__name__)
except Exception as error:
    print("MyUsefulCl@ss: ", error)

