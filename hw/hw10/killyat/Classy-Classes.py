class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def getInfo(self):
        return f"{self.name}s age is {self.age}"

if __name__ == "__main__":
    person = Person("john", 34)
    print(person.getInfo)