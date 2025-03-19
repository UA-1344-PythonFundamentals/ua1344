def day_number(number):
    match number:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednasday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            raise ValueError("The number must be between 1 and 7")


try:
    number = int(input("Enter a day number "))
    day_number(number)
except ValueError as err:
    print(err)
