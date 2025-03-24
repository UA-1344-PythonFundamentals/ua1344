def day_of_the_week(num):
    try:
        num = int(num)
        match num:
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
            case _:
                raise Exception("Wrong input! Please enter a natural number from 1 to 7")
    except ValueError:
        return "You entered not a natural number."
    except Exception as e:
        return e

if __name__ == '__main__':
    n = input("Enter a a natural number from 1 to 7: ")
    print(day_of_the_week(n))