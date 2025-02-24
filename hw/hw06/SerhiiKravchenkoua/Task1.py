even_div2 = []
odd_div3 = []
not_div2_3 = []

for num in range(1, 11):
    if num % 2 == 0:
        even_div2.append(num)
    elif num % 2 != 0 and num % 3 == 0:
        odd_div3.append(num)
    elif num % 2 != 0 and num % 3 != 0:
        not_div2_3.append(num)


print("Парні числа, які діляться на 2:", even_div2)
print("Непарні числа, які діляться на 3:", odd_div3)
print("Числа, які не діляться ні на 2, ні на 3:", not_div2_3)