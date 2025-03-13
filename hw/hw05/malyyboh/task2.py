user_input_number = int(input("Please enter the number: "))

lst_fibonacci_numbers = [0, 1]

if user_input_number >= 1:
    while lst_fibonacci_numbers[-1] + lst_fibonacci_numbers[-2] < user_input_number:
        lst_fibonacci_numbers.append(
            lst_fibonacci_numbers[-1] + lst_fibonacci_numbers[-2]
        )
    print(lst_fibonacci_numbers)
elif user_input_number == 0:
    print(0)
