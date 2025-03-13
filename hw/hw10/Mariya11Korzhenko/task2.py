class Human():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")
    
    @staticmethod
    def get_arbitrary_msg():
        return "This is arbitrary msg"
    
    @classmethod
    def get_species(cls):
        return "Homosapiens"
    


    
