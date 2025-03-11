def getDayOfWeek(number):
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
        return f"The day is: {days[number]}"
    else:
        raise ValueError("Invalid number! Enter a number between 1 and 7.")


def main():
    while True:
        try:
            number = int(input("Enter a number from 1 to 7: "))
            result = getDayOfWeek(number)
            print(result)
            break 
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

main()
