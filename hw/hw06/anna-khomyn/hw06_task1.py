div_by_2 = list()
div_by_3 = list()
not_div_by_2_3 = list()

for x in range(1, 11):
    if x % 2 == 0:
        div_by_2.append(x)
    elif x % 3 == 0:
        div_by_3.append(x)
    else:
        not_div_by_2_3.append(x)

print("Even numbers that are divisible by 2:\t\t", div_by_2)
print("Odd numbers, which are divisible by 3:\t\t", div_by_3)
print("Numbers that are not divisible by 2 and 3:\t", not_div_by_2_3)