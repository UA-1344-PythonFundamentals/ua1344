class Employee:
    """
    This class represents an employee of a company.
    """
    counter = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
        
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_counter(cls):
        print(f"Number of employees: {cls.counter}")
        
    @staticmethod
    def display_class_info():
        print(f"Class name: {Employee.__name__}\n")
        print(f"Class namespace: {Employee.__dict__}\n")
        print(f"Class module: {Employee.__module__}\n")
        print(f"Class base: {Employee.__base__}\n")
        print(f"Class doc: {Employee.__doc__}\n")
    
        
        
    
employee1 = Employee("John", 50000)
employee2 = Employee("Jane", 60000)
employee3 = Employee("Jim", 70000)

employee1.display_info()
employee2.display_info()
employee3.display_info()   

Employee.display_counter()
Employee.display_class_info()
