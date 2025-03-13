list_1 = [1, 3, 5]
list_1 = [float(digit) for digit in list_1]
print(list_1)


n = int(input("Введіть число n: "))
fib_num = [0, 1]

for i in range(2, n):
    next_fib_num = fib_num[-1] + fib_num[-2]
    if next_fib_num >= n:
        break
    fib_num.append(next_fib_num)

print(fib_num)


n = int(input("Введіть число n: "))

a, b = 0, 1
fib = [a, b]

while True:
    next_fib = a + b
    if next_fib >= n:
        break
    fib.append(next_fib)
    a, b = b, next_fib

print(fib)


n = int(input("Введіть число: "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"Факторіал {n} дорівнює {factorial}")