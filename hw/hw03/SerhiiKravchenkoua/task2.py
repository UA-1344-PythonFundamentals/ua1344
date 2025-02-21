import math

numeric = 5864

conversion_to_list = [int(d) for d in str(numeric)]
result = math.prod(conversion_to_list)
revers_number = int(str(numeric) [::-1])
sorted_digits = int(''.join(map(str, sorted(conversion_to_list))))

print(result)
print(revers_number)
print(sorted_digits)

