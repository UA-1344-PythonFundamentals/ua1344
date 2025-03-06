number = input("Enter a four-digit number: ")

# check number
if len(number) == 4 and number.isdigit():
    # convert string to list of integers
    digits = [int(digit) for digit in number]
    
    # find product of digits
    product = 1
    for digit in digits:
        product *= digit
    
    # reverse number
    reversed_number = number[::-1]
    
    # sort digits
    sorted_digits = sorted(digits)
    sorted_number = ''.join(map(str, sorted_digits))
    
    # result
    print(f"Product of digits: {product}")
    print(f"Reversed number: {reversed_number}")
    print(f"Sorted digits: {sorted_number}")
else:
    print("Only 4 numbers!")
