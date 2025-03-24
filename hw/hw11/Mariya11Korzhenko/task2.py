def give_day_of_week(day_number):
   match day_number:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _:
           raise ValueError("Incorrect day number")
       

def main():
    day_number = int(input("Enter the day number: "))
    print(give_day_of_week(day_number))

main()