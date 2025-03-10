#Task1
class Polygon:
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        
    def area(self):
        return self.width * self.height

class Rectangle(Polygon):
    pass

rect = Rectangle(5, 8)
print(rect.area())
    
#Task 2
class Human:
    def __init__(self, name):
        self.name = name
        
    def message(self):
        print(f"Hello {self.name}. Welcome")
        
    @classmethod
    def species(cls):
        return "Species: Homosapiens"
    
    @staticmethod
    def arbitary_message():
        return "This is arbitary message"
    
person = Human("Diana")
person.message()
print(Human.species())
print(Human.arbitary_message())

#Task 3
class Employee:
    employee_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        Employee.employee_count += 1
        
    @classmethod
    def get_count(cls):
        return cls.employee_count
    
employee1 = Employee("Jack", 20000)
employee2 = Employee("Lucy", 34000)
employee3 = Employee("Mike", 23000)

print(f"Total number of employees: {Employee.get_count()}")
print(f"Base class {Employee.__base__}")
print(f"Class namespace {Employee.__dict__}")
print(f"Class name {Employee.__name__}")
print(f"Module {Employee.__module__}")
print(f"Documentation {Employee.__doc__}")