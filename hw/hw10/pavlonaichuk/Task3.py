class Employee:
    count = 0 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def totalEmployees(cls):
        print(f"Total number of employees: {cls.count}")

    def employeeInfo(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("John", 2000)
emp2 = Employee("Doe", 5000)

emp1.employeeInfo()
emp2.employeeInfo()
Employee.totalEmployees()

print("\nClass Metadata:")
print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
