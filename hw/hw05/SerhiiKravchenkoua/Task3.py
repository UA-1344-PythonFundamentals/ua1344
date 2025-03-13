num = int(input("Enter a number for the factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"factorial {num} = {factorial}")