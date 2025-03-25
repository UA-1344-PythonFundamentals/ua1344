class Employee:
    # Класовий атрибут для підрахунку кількості працівників
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name  # Ім'я працівника
        self.salary = salary  # Зарплата працівника
        Employee.total_employees += 1  # Збільшуємо лічильник при створенні нового працівника

    # Метод для виведення загальної кількості працівників
    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    # Метод для виведення інформації про кожного працівника
    def print_employee_info(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

# Приклад використання:
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)
employee3 = Employee("Charlie", 55000)

# Виведення інформації про кожного працівника
employee1.print_employee_info()
employee2.print_employee_info()
employee3.print_employee_info()

# Виведення загальної кількості працівників
Employee.print_total_employees()

# Додаткова інформація про клас
print("Base classes:", Employee.__bases__)  # Базові класи
print("Class dictionary (__dict__):", Employee.__dict__)  # Простір імен класу
print("Class name (__name__):", Employee.__name__)  # Ім'я класу
print("Module name (__module__):", Employee.__module__)  # Модуль, в якому визначено клас
print("Class documentation (__doc__):", Employee.__doc__)  # Документація класу
