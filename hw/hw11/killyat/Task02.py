def get_day_of_week(number):
    try:
        number = int(number)
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        if number in days:
            return days[number]
        elif number >= 8:
            return "Number out of week range"
        else:
            raise ValueError("Please enter a valid number")
    except ValueError:
        return "Invalid input: Please enter a number"

number_input = input("Enter a number (1-7): ")
result = get_day_of_week(number_input)
print(result)