# Task 2
# Create a class Human, everyone has a name, create a method in the class that displays a welcome 
# message to each person. Create a class method in the class that returns information that 
# it is a species of "Homosapiens". And in the class create a static method that returns an arbitrary message.

class Human:  
    def __init__(self, name):  
        self.name = name  

    def welc_mesg(self):  
        return "Welcome " + self.name
    
    @classmethod
    def info_mesg(cls):
        return "You are  Homosapiens"
        
    # a static method that returns a message  
    @staticmethod
    def mesg():  
        return "Hello world"
    

person = Human("Jack")
print(person.welc_mesg())
print(person.info_mesg())
print(person.mesg())