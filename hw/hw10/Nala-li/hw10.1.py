class Polygon:
    def __init__(self, sides):
        self.sides = sides  # кількість сторон

# Клас для прямокутника, що спадкується
class Rectangle(Polygon):
    def __init__(self, length, width):
        # Виклик конструктора батьківського класу
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


if __name__ == "__main__":
    rect = Rectangle(5, 3)

    print(f"Площа прямокутника: {rect.area()}")


def species():
    return "Це вид Homo sapiens."


class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привіт, {self.name}!"

    @classmethod
    def species(cls):
        return "Вид Homo sapiens."

    @staticmethod
    def random_message():
        return "Всі люди мають розум!"


if __name__ == "__main__":
    human1 = Human("Алекс")
    human2 = Human("Ірина")

    print(human1.greet())
    print(human2.greet())

    print(Human.species())
    print(human1.species())
    print(human2.species())

    print(Human.random_message())


class Employee:
    """
    Клас співробітники, який зберігає їх ім'я, зарплату,
    методи для їх персонального відображення
    і підрахунку загальної чисельності.
    """
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        """Метод для відображення інформації про співробітника."""
        return f"Им'я: {self.name}, Зарплата: {self.salary}"

    @classmethod
    def get_employee_count(cls):
        """Метод для отримання кількості співробітників."""
        return cls.employee_count


if __name__ == "__main__":
    emp1 = Employee("Олексій", 50000)
    emp2 = Employee("Ірина", 60000)
    emp3 = Employee("Дмитро", 70000)

    print(emp1.display_info())
    print(emp2.display_info())
    print(emp3.display_info())

    print(f"Загальна кількість співробітників: {Employee.get_employee_count()}")  # 3

    print(f"Базові класи: {Employee.__bases__}")
    print(f"Простір імен класу: {Employee.__dict__}")
    print(f"Им'я класу: {Employee.__name__}")
    print(f"Им'я модулю: {Employee.__module__}")
    print(f"Документація класу: {Employee.__doc__}")
    print(f"Документація методу display_info: {Employee.display_info.__doc__}")
    print(f"Документація методу get_employee_count: {Employee.get_employee_count.__doc__}")


