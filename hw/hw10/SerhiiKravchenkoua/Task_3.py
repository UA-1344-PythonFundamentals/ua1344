class Employee:

    employee_count = 0

    def  __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print(f"Employee name {self.name}, Salary {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total Employees {cls.employee_count}")

# emp1 = Employee("Serhii", 10000)
# emp2 = Employee("Volo", 5000)

# emp1.display_employee()
# emp2.display_employee()
#
# Employee.total_employees()