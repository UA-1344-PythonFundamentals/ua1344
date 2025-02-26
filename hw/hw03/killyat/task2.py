number = 543423
digits = [int(d) for d in str(number)] 
product = 1
for digit in digits:
    product *= digit
print(f"Добуток цифр: {product}")
reversed_number = int(''.join(str(d) for d in digits[::-1]))
print(f"Число у зворотному порядку: {reversed_number}")
sorted_digits = sorted(digits)
sorted_number = int(''.join(str(d) for d in sorted_digits))
print(f"Цифри у порядку зростання: {sorted_number}")