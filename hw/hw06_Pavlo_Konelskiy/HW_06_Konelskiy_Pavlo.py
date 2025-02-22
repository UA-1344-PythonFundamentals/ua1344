#Task_01

even_numbers = []
odd_numbers = []
not_divisible_numbers = []

for num in range(1, 11):
    if num % 3 == 0:
        odd_numbers.append(num)

    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 3 != 0:
        not_divisible_numbers.append(num)

print("Even numbers that are divisible by 2:", even_numbers)
print("Odd numbers, which are divisible by 3:", odd_numbers)
print("Numbers that are not divisible by 2 and 3:", not_divisible_numbers)

#Task_02
while True:
    login = input("Login: ")
    if login == "First":
        print("Hello!")
        break
    else:
        print("Error: wrong login!")