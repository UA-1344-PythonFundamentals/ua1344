class Employee:
    """A class to represent a Employee."""

    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def get_information_employee(self):
        print(f"Employee name: {self.name}\nEmployee salary: {self.salary}")

    @classmethod
    def total_number_employees(cls):
        print(f"The total number of employees: {Employee.counter}")


first_employee = Employee("Bohdan Danylko", 2000)
second_employee = Employee("Petro Melnyk", 2500)

Employee.total_number_employees()

first_employee.get_information_employee()
second_employee.get_information_employee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
