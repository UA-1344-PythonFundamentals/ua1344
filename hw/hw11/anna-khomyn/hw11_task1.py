class InputError(Exception):
    pass

def check_odd_even(number):
    try:
        number = int(number)
        if number < 0:
            raise InputError(f"The age can not be negative number {number}")
        if number % 2 == 1:
            return f"Entered age {number} is odd"
        if number % 2 == 0:
            return f"Entered age {number} is even"
    except InputError as e:
        return e
    except ValueError:
        return "You entered not a number."
    
if __name__ == '__main__':
    for x in (25, 30, -30, "35", "dsjh"):
        print(check_odd_even(x))

    age = input("\nEnter your age: ")
    print(check_odd_even(age))