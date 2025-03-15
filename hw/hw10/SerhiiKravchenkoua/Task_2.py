class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def specie(cls):
        return "Homosapiens"

    @staticmethod
    def massage():
        return "Have a nice day!"

# person1 = Human("Serhii")
# person1.greet()
#
# print(Human.specie())
# print(Human.massage())