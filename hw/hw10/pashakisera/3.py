# Task3
# Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees, as well
# as a method that prints the total number of employees and a method that displays information
# about each employee in particular, namely the name and salary.
#
# In addition to creating a class, display information about the base classes from which the employee class
# is inherited (__base_), the class namespace (_dict__), the class name (name_,
# the module name in which the class is defined (module_, the documentation bar (_doc_)


class Employee:
    """Class has characteristics such as name and salary"""
    __id = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__id += 1

    def employee_info(self):
        return "Employee " + self.name + " with salary " + str(self.salary)

    @classmethod
    def counter(cls):
        return "You have " + str(cls.__id) + " employees"

    @staticmethod
    def class_info():
        print("Base class: " + str(Employee.__base__))
        print("Namespace: " + str(Employee.__dict__))
        print("Class name: " + str(Employee.__name__))
        print("Module name: " + str(Employee.__module__))
        print("Documentation: " + str(Employee.__doc__))


employee1 = Employee("John Dou", 500)
print(employee1.employee_info())
print(Employee.counter())

employee2 = Employee("Antonio Banderas", 700)
print(employee2.employee_info())
print(Employee.counter())

print(Employee.class_info())