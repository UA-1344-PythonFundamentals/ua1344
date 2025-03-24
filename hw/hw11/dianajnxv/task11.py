#Task1
def age(age):
    try:
        if age < 0:
            print("An error occurred: age cannot be negative")
            return
        
        if age % 2 == 0:
            print("Age is even")
        else:
            print("Age is odd")
    
    except TypeError:
        print("An error occurred: invalid type, expected an integer")
        
age_input = int(input("Please enter your age: "))

age(age_input)      


#Task2
def days(day):
    try:
        if day >= 8 or day < 1:
            print("Entered number must be between 1 and 7") 
            return
        
        if day == 1:
            print("Monday")
        elif day == 2:
            print("Tuesday")
        elif day == 3:
            print("Wednesday")
        elif day == 4:
            print("Thursday")
        elif day == 5:
            print("Friday")
        elif day == 6:
            print("Saturday")
        else:
            print("Sunday")
        
    except TypeError:
        print("An error occurred: invalid type, expected an integer")

try:
    entered_day = int(input("Please enter a number: "))
    days(entered_day)
except ValueError:
    print("Invalid input: please enter an integer.")
