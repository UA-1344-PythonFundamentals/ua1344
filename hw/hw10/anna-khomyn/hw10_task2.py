class Human:
    __species = "Homosapiens"
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}!")
    
    @classmethod
    def species(cls):
        return f"Species: \'{cls.__species}\'"
    
    @staticmethod
    def say_something_smart():
        print('\n"The greatness of humanity is not in being human, but in being humane.”\n - Mahatma Gandhi')
        

if __name__ == '__main__':

    anna = Human("Anna")
    anna.greet()

    print(f"Call from instance:  {anna.species() = }")
    print(f"Call from class:  {Human.species() = }")

    anna.say_something_smart()