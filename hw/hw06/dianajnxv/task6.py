#task 1 
numbers = range(1, 11)

even_numbers = [num for num in numbers if num % 2 == 0]
        
odd_numbers = [num for num in numbers if num % 3 == 0]

not_divisible = [num for num in numbers if num % 2 != 0 and num % 3 != 0]

print(even_numbers)
print(odd_numbers)
print(not_divisible)

        
        
#task 2

while True:
    login = input("Enter login: ")
    if login == "First":
        print("Welcome!")
        break
    else: 
        print("Error")
    