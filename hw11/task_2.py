def get_day_of_week():
    try:
        # Отримуємо вхідне значення від користувача
        day_number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
        
        # Перевіряємо, чи число в межах від 1 до 7
        if 1 <= day_number <= 7:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"The day of the week is: {days[day_number - 1]}")
        else:
            print("Invalid number! Please enter a number between 1 and 7.")
    
    except ValueError:
        # Якщо введено нечислове значення
        print("Invalid input! Please enter a number between 1 and 7.")

# Викликаємо функцію
get_day_of_week()