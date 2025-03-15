class Human:
    def __init__(self, name):
        self.name = name
        
    def welcome(self):
        print(f"Hello, {self.name}!")
        
    @classmethod
    def species():
        print("Homosapiens species")

    @staticmethod
    def arbitrary_msg():
        print("This is an arbitrary message")
