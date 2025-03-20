# Create a class Human, each has a name, create a method in the class that displays a greeting message to each person. Create a method in the class that returns information that this is the species "Homosapiens". And in the class, create a static method that returns a random message.

class Человек:
    def __init__(self, имя):
        self.имя = имя

    def приветствие(self):
        print(f"Привет, {self.имя}!")

    def информация_о_виде(self):
        return "Это вид: Homosapiens"

    @staticmethod
    def сообщение():
        return "Статическое сообщение"


человек1 = Человек("Максим")
человек1.приветствие()
print(человек1.информация_о_виде())

print(Человек.сообщение()) # staticmethod
