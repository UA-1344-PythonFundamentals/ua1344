def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number < 1 or number > 7:
        raise ValueError("Entered number is out of range. Please enter a number between 1 and 7.")

    return days[number]

def main():
    try:
        number = int(input("Please enter a number (1-7) to get the corresponding day of the week: "))
        day = get_day_of_week(number)
        print(f"The day corresponding to number {number} is {day}.")
    except ValueError as e:
        print(f"Error: {e}")

main()
