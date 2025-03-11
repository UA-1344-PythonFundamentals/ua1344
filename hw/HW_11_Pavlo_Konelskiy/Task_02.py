def weekday():
    days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    try:
        day_number = int(input("Enter a number for the day of the week: "))

        if day_number in days:
            print(f"{days[day_number]}")
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a number.")

weekday()