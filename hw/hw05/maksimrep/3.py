num = int(input("Enter number for calculation: "))

# list for numbers from 1 to num
numbers = []
for i in range(1, num + 1):
    numbers.append(i)

# variable for factorial
result = 1
for value in numbers:
    result *= numbers[value - 1]

print(f"Factorial: {result}")
