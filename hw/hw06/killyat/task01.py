for i in range(1, 11):
    if i % 2 == 0:
        print(f"Even number divisible by 2: {i}")

for i in range(1, 11):
    if i % 2 != 0 and i % 3 == 0:
        print(f"Odd number divisible by 3: {i}")

for i in range(1, 11):
    if i % 2 != 0 and i % 3 != 0:
        print(f"Number not divisible by 2 and 3: {i}")