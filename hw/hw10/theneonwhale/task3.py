class Employee:
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def print_total_employees(self):
        print(f"Total number of employees: {Employee.counter}")

    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

emp1 = Employee("Kitana", 50000)
emp2 = Employee("Jade", 60000)

emp1.display_employee_info()
emp2.display_employee_info()

emp1.print_total_employees()

print("\nClass-related information:")
print(f"Base class: {Employee.__base__}")
print(f"Class dictionary: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
