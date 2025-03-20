#Create an employee class. Each employee has characteristics such as name and salary. The class should have a counter that calculates the total number of employees, as well as a method that prints the total number of employees, and a method that displays information about each employee in particular, namely name and salary.
#
#In addition to creating the class, print information about the base classes from which the employee class is inherited (_base_), the class namespace (_dict), the class name (_name_), the name of the module in which the class is defined (_module__), the documentation panel (_doc_)

class Сотрудник:
    
    количество_сотрудников = 0

    def __init__(self, имя, зарплата):
        self.имя = имя
        self.зарплата = зарплата

        Сотрудник.количество_сотрудников += 1

    def информация_о_сотруднике(self):
        return f"Сотрудник: {self.имя}, Зарплата: {self.зарплата} $."

    @classmethod
    def общее_количество_сотрудников(cls):
        print(f"Общее количество сотрудников: {cls.количество_сотрудников}")


сотрудник1 = Сотрудник("Максим", 50000)
сотрудник2 = Сотрудник("Любомир", 60000)
сотрудник3 = Сотрудник("Третий", 55000)

print(сотрудник1.информация_о_сотруднике())
print(сотрудник2.информация_о_сотруднике())
print(сотрудник3.информация_о_сотруднике())

# Выведем общее количество сотрудников
Сотрудник.общее_количество_сотрудников()

# о классе
print(f"Базовые классы: {Сотрудник.__bases__}")  # Базовые классы
print(f"Пространство имен класса: {Сотрудник.__dict__}")  # Пространство имен
print(f"Имя класса: {Сотрудник.__name__}")  # Имя класса
print(f"Имя модуля: {Сотрудник.__module__}")  # Имя модуля
print(f"Документация класса: {Сотрудник.__doc__}")  # Документация класса
