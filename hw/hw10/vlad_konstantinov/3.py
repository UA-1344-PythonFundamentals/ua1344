class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def get_info(self):
        return f"Employee Name: {self.name} Salary: {self.salary}"

    @classmethod
    def get_count(cls):
        return f"Employee total {cls.employee_count}"


def class_info(cls):
   print(f"Base class: {cls.__base__}")
   print(f"Namespace: {cls.__dict__}")
   print(f"Class name: {cls.__name__}")
   print(f"Module name: {cls.__module__}")
   print(f"Documentation: {cls.__doc__}")

emp1 = Employee("J", 2000)
emp2 = Employee("A", 2000)

print(emp1.get_info())
print(emp2.get_info())
print(Employee.get_count())

class_info(Employee)