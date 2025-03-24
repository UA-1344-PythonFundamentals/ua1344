def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        return "Entered age is even."
    else:
        return "Entered age is odd."

def main():
    try:
        age = int(input("Please enter your age: "))
        result = check_age(age)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

main()
