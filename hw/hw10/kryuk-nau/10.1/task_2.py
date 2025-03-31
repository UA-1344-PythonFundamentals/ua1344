class Human:
    def __init__(self, name):
        self.name = name  # Атрибут для збереження імені людини

    # Інстанс метод для привітання людини
    def greet(self):
        print(f"Welcome, {self.name}!")

    # Клас метод, що повертає вид людини
    @classmethod
    def species(cls):
        return "Homo sapiens"

    # Статичний метод для виведення довільного повідомлення
    @staticmethod
    def message():
        return "This is a static message."

# Приклад використання:

# Створення об'єкта класу Human
person = Human("Alice")

# Виклик інстанс методу для привітання
person.greet()  # Виведе: Welcome, Alice!

# Виклик клас методу для отримання інформації про вид
print(Human.species())  # Виведе: Homo sapiens

# Виклик статичного методу для отримання довільного повідомлення
print(Human.message())  # Виведе: This is a static message.
