evenNumbers = []
oddDivisibleBy3 = []
neitherDivisibleBy2Nor3 = []

for i in range(1, 11):
    if i % 2 == 0:
        evenNumbers.append(i)
    if i % 2 != 0 and i % 3 == 0:
        oddDivisibleBy3.append(i)
    if i % 2 != 0 and i % 3 != 0:
        neitherDivisibleBy2Nor3.append(i)

print("Even numbers divisible by 2:", evenNumbers)
print("Odd numbers divisible by 3:", oddDivisibleBy3)
print("Numbers not divisible by 2 or 3:", neitherDivisibleBy2Nor3)