n = int(input("Enter number for calculating factorial: "))

# Calculate factorial for given number
for i in range (n):
    if i == 0:
        factorial = 1
        msg = str(n) +"! = 1"
    else:
        factorial *= i
        msg += " * " + str(i)
else:
    print(msg + " = " + str(factorial))

# Here is another way, which holds the whole factorial sequence using a list
factorial_num = []
for i in range (n):
    if i == 0:
        factorial_num.append(1)
    else:
        factorial_num.append(i * factorial_num[i-1])
print(f"Factorial sequence:\t {factorial_num}")