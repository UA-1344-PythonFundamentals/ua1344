n = int(input("Enter number for calculating the Fibonacci numbers: "))

fibonacci_num = [0, 1]
while fibonacci_num[-1] + fibonacci_num[-2] <= n:
    fibonacci_num.append(fibonacci_num[-1] + fibonacci_num[-2])

print(fibonacci_num)