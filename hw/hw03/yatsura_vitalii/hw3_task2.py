num = input("Enter a four-digit number: ")

#Part 1
num_product_char = 1

for i in num:
    num_product_char *= int(i)

print(num_product_char)


#Part 2
num_reversed = num[::-1]

print(num_reversed)


#Part 3
sorted_num = "".join(sorted(num))

print(sorted_num)