import inspect

class Employee:
    _count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee._count += 1

    @classmethod
    def total_employees(cls):
        return cls._count

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def display_base_classes(cls):
        return f"Base classes: {cls.__bases__}"

    @classmethod
    def display_namespace(cls):
        return f"Namespace: {cls.__dict__}"

    @classmethod
    def display_class_name(cls):
        return f"Class name: {cls.__name__}"

    @classmethod
    def display_module_name(cls):
        return f"Module name: {cls.__module__}"

    @classmethod
    def display_documentation(cls):
        return f"Documentation: {cls.__doc__ or 'No documentation'}"

if __name__ == "__main__":
    emp1 = Employee("Alice", 5000)
    emp2 = Employee("Bob", 6000)
    print(Employee.total_employees())
    print(emp1.display_info())
    print(Employee.display_base_classes())
    print(Employee.display_namespace())
    print(Employee.display_class_name())
    print(Employee.display_module_name())
    print(Employee.display_documentation())