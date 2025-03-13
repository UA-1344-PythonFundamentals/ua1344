class Ball(object):
  """Regular Ball Super Ball"""
  def __init__(self, type = "regular"):
    self.ball_type = type


import random

class Ghost(object):
    """Color Ghost"""
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
       self.color = random.choice(Ghost.colors)



class Human():
    """Basic subclasses - Adam and Eve"""
    def __init__(self):
        print('This is my Human')
    
class Woman(Human):
    def __init__(self):
        print('This is my Woman')
    
class Man(Human):
    def __init__(self):
        print('This is my Man')

def God():
    return (Man(), Woman())


class Person():
    """Classy Classes"""
    def __init__(self, name,age):
        self.__info= f"{name}s age is {age}"
        
    @property
    def info(self):
        return self.__info
    


import math

class Sphere():
    """Building Spheres"""
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass
        
    def get_radius(self):
        return self.__radius
    
    def get_mass(self):
        return self.__mass
        
    def get_volume(self):
        return round(4/3*math.pi*(self.get_radius()**3), 5)
    
    def get_surface_area(self):
        return round(4*math.pi*(self.get_radius()**2), 5)
    
    def get_density(self):
        return round(self.get_mass()/self.get_volume(),5)


import re

def class_name_changer(cls, new_name):
    """Python's Dynamic Classes """
    if(new_name == ""):
        raise ValueError("New class name must be a non-empty string.")
    elif(new_name[0] != new_name[0].capitalize()):
         raise ValueError("Class should start from capital letter")
    elif(type(new_name[0]) == int):
        raise ValueError(f"Failed to rename class: {e}")
    if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", new_name):
        raise ValueError("New class name must start with an uppercase letter and contain only letters and digits.")
    else:
        cls.__name__ = new_name
        