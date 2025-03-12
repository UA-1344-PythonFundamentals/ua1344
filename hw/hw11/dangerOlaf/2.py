# Task 2.
# Write a program that analyzes the entered number and, depending on the number, gives the day of the week 
# that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). 
# Take into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data.

class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return repr(self.data)


def check_day(day):
    try:
        if int(day) <= 0 or int(day) > 7:
            raise CustomError("Your is day incorrect!")
    
    except CustomError as e:
        return e
    
    except ValueError:
        return "Please enter an integer"
    
    
    match int(day):
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
    

day = input("Please enter a number of a day: ")

print(check_day(day))