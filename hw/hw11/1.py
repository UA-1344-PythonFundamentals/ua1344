def check_age():
    try:
        age_input = int(input("Enter age: "))
        if age_input <= 0:
            raise ValueError("Negative")
        elif age_input % 2 == 0:
            print(f"Your age is even")
        else:
            print(f"Your age is odd")
    except ValueError as e:
        print(f"Error: {e}")


def weather():
    days = { 1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
            }
    try:
        a = int(input("Enter a day: "))
        if a not in days:
            raise ValueError("The number not from 1 to 7")
        print(f"Day of the week: {days[a]}")
    except ValueError as e:
        print(f"Error: {e}")

check_age()
weather()