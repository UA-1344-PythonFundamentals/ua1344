divisible_by_2_lst = []
divisible_by_3_lst = []
not_divisible_by_2_and_3_lst = []

for i in range(1, 11):
    if i % 2 == 0:
        divisible_by_2_lst.append(i)
    elif i % 3 == 0:
        divisible_by_3_lst.append(i)
    else:
        not_divisible_by_2_and_3_lst.append(i)

print(f"Even numbers that are divisible by 2: {divisible_by_2_lst}")
print(f"Odd numbers that are divisible by 3: {divisible_by_3_lst}")
print(f"Numbers that are not divisible by 2 and 3: {not_divisible_by_2_and_3_lst}")
