n = int(input("Enter a number to calculate the factorial: "))
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0 or n == 1:
    print(f"{n}! = 1")
else:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")