number = 2413

product_of_number = (
    (number // 1000) * (number // 100 % 10) * (number // 10 % 10) * (number % 10)
)
print(product_of_number)


number_reverse = str(number)[::-1]
print(number_reverse)


sort_number = list(str(number))
sort_number.sort()
sort_number = int("".join(sort_number))
print(sort_number)
