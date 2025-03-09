class Employee:
    """Class for representing the company's employees"""

    employee_count = 0

    def __init__(self, name, salary):
        """Initialize employee attributes"""
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        """Display employee information"""
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: ${self.salary}")

    @classmethod
    def get_total_employees(cls):
        """Return the total number of employees"""
        print(f"Total number of employees {cls.employee_count}")

emp_01 = Employee("Ivan", 100000)
emp_02 = Employee("Oksana", 25000)

emp_01.display_employee_info()
emp_02.display_employee_info()

Employee.get_total_employees()

print("Base class:", Employee.__base__)  
print("Class namespace:", Employee.__dict__)  
print("Class name:", Employee.__name__)  
print("Class module:", Employee.__module__)  
print("Class documentation:", Employee.__doc__)  