integer_list = [1, 20, 300, 6, 234, 566, 12, 34, 56, 78, 90, 100]

float_list = []
for num in integer_list:
    float_list.append(float(num))

print("Original list:", integer_list)
print("Converted list:", float_list)
