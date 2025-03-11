def processAge(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."


def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            result = processAge(age)
            print(result)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            
main()