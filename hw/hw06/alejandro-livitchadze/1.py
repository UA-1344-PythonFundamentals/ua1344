l = list(range(1, 11))
divisible_2 = []
divisible_3 = []
rest = []
for i in l:
    if i % 2 == 0:
        divisible_2.append(i)
    elif i % 3 == 0:
        divisible_3.append(i)
    else:
        rest.append(i)
print(f"Divisible by 2: {divisible_2}")
print(f"Divisible by 3: {divisible_3}")
print(f"Rest: {rest}")