def check_age():
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age cannot be negative")
        elif age % 2 == 0:
            print("Age is even")
        else:
            print("Age is odd")
    except ValueError:
        print("Invalid input. Please enter a number.")

check_age()       