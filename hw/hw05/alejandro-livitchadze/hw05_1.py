int_list = list(range(0, 10))

print(int_list)

for i in int_list:
    int_list[i] = float(int_list[i])

print(int_list)