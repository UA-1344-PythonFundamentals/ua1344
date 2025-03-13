class Human:
    species = "Homosapienc"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

    @classmethod
    def get_species(cls):
        return f"I am a {cls.species}"

    @staticmethod
    def random_message():
        return "Random words in message"


person = Human("Pavlo")
person.greet()

print(Human.get_species())

print(Human.random_message())