# Отримуємо число
num = int(input("Enter a number: "))

# Початкове значення факторіалу
factorial = 1

# Обчислюємо факторіал за допомогою циклу
for i in range(1, num + 1):
    factorial *= i


print(f"{num}! =", factorial)
