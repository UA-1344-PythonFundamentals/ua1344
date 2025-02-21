num = input("Enter a four-digit number: ")

if len(num) != 4 or not num.isdigit():
    print("Invalid input! Please enter a four-digit number.")
else:
    num = int(num)
    digits = [int(d) for d in str(num)]

    product = 1
    for d in digits:
        product *= d

    reversedNum = int(str(num)[::-1])
    sortedDigits = ''.join(sorted(str(num)))

    print("Product of digits:" , product)
    print("Reversed number: " , reversedNum)
    print("Sorted digits: ", sortedDigits)