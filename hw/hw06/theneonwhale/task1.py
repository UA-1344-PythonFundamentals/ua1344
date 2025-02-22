even_numbers = []
odd_div_by_3 = []
other = []

for num in range(1, 11):
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 3 == 0:
        odd_div_by_3.append(num)
    else:
        other.append(num)

print(f"Even numbers divisible by 2: {even_numbers}")
print(f"Odd numbers divisible by 3: {odd_div_by_3}")
print(f"Numbers not divisible by 2 or 3: {other}")
