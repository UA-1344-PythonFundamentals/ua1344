class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello {self.name}")

    @classmethod
    def output_species(cls):
        print("Human beings belong to the species 'Homosapiens'")

    @staticmethod
    def stat_message():
        print("Message from the static method")


h = Human("Bohdan")
h.welcome()
Human.output_species()
h.stat_message()
