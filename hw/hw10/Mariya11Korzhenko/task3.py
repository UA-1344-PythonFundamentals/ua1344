class Employee():
    """Employee class description"""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count +=1

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def total_employees(cls):
        return f"Total number of employees: {cls.count}"
    
    @staticmethod
    def class_info():
        print(f"Base class: {Employee.__base__}")
        print(f"Namespace: {Employee.__dict__}")
        print(f"Class name: {Employee.__name__}")
        print(f"Module name: {Employee.__module__}")
        print(f"Documentation: {Employee.__doc__}")

emp1 = Employee("Hanna", 100)
emp2 = Employee("Tommy", 150)

print(emp1.display_info())
print(emp2.display_info())
print(Employee.total_employees())

Employee.class_info()
