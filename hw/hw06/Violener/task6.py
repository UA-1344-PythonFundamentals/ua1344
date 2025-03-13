#task1
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
odd_div_by_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 == 0]
not_div_by_2_3 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]

print(even_numbers)

#task2
correct_login = "First"
while True:
    user_input = input("enter your login: ")
    if user_input == correct_login:
        print("good!")
        break
    else:
        print("wrong login")