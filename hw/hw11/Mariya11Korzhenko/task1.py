class AgeSorting():

    def __init__(self, age):
        if(age<0):
            raise ValueError("Age should be positive number")
        self.__age = age

    def is_odd_even(self):
        print(f"Age {self.__age} is even" if self.__age % 2 == 0 else f"Age {self.__age} is odd")


enteredAge = int(input("Enter the age: "))
try:
    AgeSorting(enteredAge).is_odd_even()
except ValueError as e:
    print(f"Error: {e}")

