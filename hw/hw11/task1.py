def get_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return "The age is even"
    else:
        return "The age is odd"


try:
    user_age = int(input("Please enter your age: "))
    print(get_age(user_age))
except ValueError as err:
    print(err)
