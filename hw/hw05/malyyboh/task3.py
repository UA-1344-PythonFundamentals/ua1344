user_input_number = int(input("Please enter the number: "))

if user_input_number >= 0:
    factorial = 1
    for i in range(1, user_input_number + 1):
        factorial *= i
    print(factorial)
else:
    print("Incorrect input")
