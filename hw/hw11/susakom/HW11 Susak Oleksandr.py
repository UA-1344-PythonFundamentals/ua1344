# HW11 Susak Oleksandr

def get_age(age):
    age=int(age)
    if age <=0:
        raise ValueError("Age cannot be negative or zero. Please enter a positive number.")
    if (age % 2) == 0:
        return "Your age is even"
    else:
        return "Your age is odd"

age = input("Enter age: ")
try:
    print(get_age(age))
except ValueError as er:
    print(er)
except TypeError as er:
    print(er)


def get_day(number_of_day):
        try:
              number_of_day = int(number_of_day)
        except ValueError:
              raise ValueError("Error: Please enter a valid number.")
        if   int(number_of_day) <= 0 or int(number_of_day) >= 8:
            raise ValueError("Error: Please enter a valid number.")
        else:
             number_of_day = int(number_of_day)
        if number_of_day == 1:
              name_of_day = "Monday"
        elif number_of_day == 2:
              name_of_day = "Tuesday"
        elif number_of_day == 3:
              name_of_day = 'Wednesday'
        elif number_of_day == 4:
              name_of_day = "Thursday"
        elif number_of_day == 5:
              name_of_day = 'Friday'
        elif number_of_day == 6:
              name_of_day = 'Saturday'
        elif number_of_day == 7:
              name_of_day = 'Sunday'
        
        return name_of_day

day_number = input("Enter number of day= ")

try:
     print(get_day(day_number))
except ValueError as er:
      print(er)
