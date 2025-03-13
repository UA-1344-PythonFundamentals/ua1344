# HW10 Susak Oleksandr

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(num_sides=4)
        self.length = int(length)
        self.width = int(width)
    def get_rectangle_area(self):
        return self.length * self.width
    


class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome {self.name}!"
    
    @classmethod
    def special_info(cls):
        return "It is a species of Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        return "This is arbitrary_message"
    


class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
        
        Employee.employee_count += 1

    def get_employee_count(self):
        return Employee.employee_count
    
print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Class documentation:", Employee.__doc__)