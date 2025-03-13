
#class Polygon:
#    def __init__(self, sides):
#        self.sides = sides
#
#class Rectangle(Polygon):
#    def __init__(self, width, height):
#        super().__init__(4)  
#        self.width = width
#        self.height = height
#
#    def area(self):
#        return self.width * self.height
#
#
#rect = Rectangle(10, 5)
#print(f"Rectangle area: {rect.area()}")
#
#
#
#class Human:
#    def __init__(self, name):
#        self.name = name
#
#    def welcome_message(self):
#        return f"Hello, {self.name}! Welcome to the world."
#
#    @classmethod
#    def species(cls):
#        return "Homosapiens"
#
#    @staticmethod
#    def arbitrary_message():
#        return "This is an arbitrary message."
#
#
#person = Human("Alice")
#print(person.welcome_message())
#print(Human.species())
#print(Human.arbitrary_message())
#
#
#
#class Employee:
#    employee_count = 0
#
#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary
#        Employee.employee_count += 1
#
#    def display_info(self):
#        return f"Employee Name: {self.name}, Salary: ${self.salary}"
#
#    @classmethod
#    def total_employees(cls):
#        return f"Total number of employees: {cls.employee_count}"
#
#
#def class_info(cls):
#    print(f"Base class: {cls.__base__}")
#    print(f"Namespace: {cls.__dict__}")
#    print(f"Class name: {cls.__name__}")
#    print(f"Module name: {cls.__module__}")
#    print(f"Documentation: {cls.__doc__}")
#
#
#emp1 = Employee("John", 5000)
#emp2 = Employee("Jane", 6000)
#
#print(emp1.display_info())
#print(emp2.display_info())
#print(Employee.total_employees())
#
#
#class_info(Employee)
#1
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)  
print(ball2.ball_type)  
#2
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost1 = Ghost()
ghost2 = Ghost()
ghost3 = Ghost()

print(ghost1.color)  
print(ghost2.color)  
print(ghost3.color)  
#3
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def creation():
    return [Man(), Woman()]
#4
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    #5
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
        return round((4/3) * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


ball = Sphere(2, 50)
print(ball.get_radius())        
print(ball.get_mass())          
print(ball.get_volume())        
print(ball.get_surface_area())  
print(ball.get_density())       
#6
import re

def rename_class(cls, new_name):
   
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError("Invalid class name. It must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name  



class MyClass:
    pass

print(MyClass.__name__)  

rename_class(MyClass, "UsefulClass")
print(MyClass.__name__)  

rename_class(MyClass, "SecondUsefulClass")
print(MyClass.__name__)  



