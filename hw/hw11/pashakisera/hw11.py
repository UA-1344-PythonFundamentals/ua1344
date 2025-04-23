def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative!")
        elif age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    except ValueError as e:
        print(f"Error: {e}")

def get_weekday():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    try:
        num = int(input("Enter a number from 1 to 7: "))
        if num not in days:
            raise ValueError("The number must be between 1 and 7!")
        print(f"Day of the week: {days[num]}")
    except ValueError as e:
        print(f"Error: {e}")


check_age()
get_weekday()