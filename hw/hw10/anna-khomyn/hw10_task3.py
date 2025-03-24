class Employee:
    """Class Employee has characteristics such as name and salary"""
    __count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.increase_counter()
    
    def __del__(self):
        Employee.decrease_counter()

    def __str__(self):
        return f"The employee {self.name} has salary {self.salary} $"
    
    def __repr__(self):
        return f"{self.name}, {self.salary}"
    
    @classmethod
    def increase_counter(cls):
        cls.__count += 1

    @classmethod
    def decrease_counter(cls):
        cls.__count -= 1

    @classmethod
    def get_count(cls):
        return cls.__count

    @staticmethod
    def print_empl_number():
        print(f"The total number of employees is {Employee.__count}")

    @classmethod
    def class_info(cls):
        print(f"{cls.__base__ = }")
        print(f"{cls.__dict__ = }")
        print(f"{cls.__name__ = }")
        print(f"{cls.__module__ = }")
        print(f"{cls.__doc__ = }")


if __name__ == '__main__':
    emp1 = Employee("Edward", 1500)
    emp2 = Employee("Viktoria", 2300)
    emp3 = Employee("Andy", 2000)
    emp4 = Employee("Ronald", 900)

    Employee.print_empl_number()

    print("I can print representation for each employee:")

    for e in (emp1, emp2, emp3, emp4):
        print('\t', repr(e))

    print("or just print employe info:")

    print('\t', emp1)

    print(f"delete employee {emp3.name}\n")
    del emp3

    print("and let's check employee counter now: ")
    print('\t', Employee.get_count())

    print("Finally, I can get some info about 'Employee' class:\n")

    Employee.class_info()