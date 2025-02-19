number = int(input("Enter a number: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i 

print(f"Factorial of {number} is: {factorial}")