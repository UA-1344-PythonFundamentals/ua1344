def process_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative!")
        return "Age is even" if age % 2 == 0 else "Age is odd"
    except ValueError as e:
        return str(e)

age_input = input("Enter your age: ")
result = process_age(age_input)
print(result)