class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return "This species is Homo sapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."


person1 = Human("Andrii")
print(person1.greeting())
print(Human.species_info())
print(Human.arbitrary_message())

person2 = Human("Jennifer")
print(person2.greeting())
