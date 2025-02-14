four_digit_number = 5471

def digits_product(number):
    digit_list = list(str(number))
    product = 1
    for i in digit_list:
        product *=int(i)
    return product

def digits_revert(number):
    return str(number)[::-1]

def digits_sort(number):
    digit_list = list(str(number))

    digit_list_upd = []
    for i in digit_list: 
        digit_list_upd.append(i)

    result = ""
    for i in sorted(digit_list_upd):
         result += str(i)
         
    return int(result)   

# result
print(digits_sort(four_digit_number))
print(digits_product(four_digit_number))
print(digits_revert(four_digit_number))
