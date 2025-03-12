# Task 1.
# Write a program that prompts the user to enter their age, and then displays a message
# stating whether the age is even or odd. The program must provide the ability to enter a negative number, 
# and in this case generate an exception. The master code should call a function that processes the information entered.

def check_age(age):
    try:
        if age <= 0:
            raise ValueError("Your age is strange!")
    except ValueError as e:
        return e
    
    return "Your age is even" if age % 2 == 0 else "Your age is odd"

age = int(input("Please enter your age: "))

print(check_age(age))