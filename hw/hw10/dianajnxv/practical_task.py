#Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")  

print(ball1.ball_type)  
print(ball2.ball_type)  

#Color-ghost
import random

class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)
        
ghost = Ghost()
print(ghost.color)
        
#Basic-subclasses-Adam-and-Eve
class Human:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)

class God:
    def create_humans(self):
        return [Man(), Woman()]

god = God()
paradise = god.create_humans()

print([str(human) for human in paradise])

#Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

john = Person("John", 34)
print(john.info)  

#Building Spheres
import math
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round((4/3) * math.pi * (self.radius ** 3), 5)

    def get_surface_area(self):
        return round(4 * math.pi * (self.radius ** 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    

ball = Sphere(2, 50)
print(ball.get_radius())        
print(ball.get_mass())          
print(ball.get_volume())        
print(ball.get_surface_area())  
print(ball.get_density()) 

#Dynamic Classes
def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise ValueError("Invalid class name")

class MyClass:
    pass

print(MyClass.__name__)  

class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__) 