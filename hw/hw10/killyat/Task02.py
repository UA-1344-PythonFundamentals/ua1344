class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return "This is a species of 'Homosapiens'."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

if __name__ == "__main__":
    human = Human("John")
    print(human.welcome_message())
    print(Human.species_info())
    print(Human.arbitrary_message())