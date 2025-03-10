class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def speciesInfo(cls):
        return f"This is a species of {cls.species}."

    @staticmethod
    def message():
        return "Humans are amazing beings!"

person = Human("Pavlo")
person.welcome()
print(Human.speciesInfo())
print(Human.message())
