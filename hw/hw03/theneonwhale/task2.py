def product_reverse_sorted():
    while True:
        num_str = input("Enter a 4-digit number: ")
        if num_str.isdigit() and len(num_str) == 4:
            break
        else:
            print("Invalid input. Please enter a valid 4-digit number.")

    product = 1
    for digit in num_str:
        product *= int(digit)
    print(f"Product of digits: {product}")

    reverse_num = num_str[::-1]
    print(f"Reversed number: {reverse_num}")

    sorted_digits = ''.join(sorted(num_str))
    print(f"Sorted digits in ascending order: {sorted_digits}")

    return

product_reverse_sorted()
