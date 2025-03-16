def process_input(age):
    try:
        if age < 0:
            raise ValueError('Negative age is provided')
        print('Age is even' if age % 2 == 0 else 'Age is odd')
    except (TypeError, ValueError) as err:
        print(err)

try:
    age = int(input("Enter your age: "))
    process_input(age)
except ValueError:
    print("Please enter a valid integer for age")