#   2
num = input("Enter a four-digit natural number: \n")
if not num.isdigit() or len(num) > 4 or len(num) < 4:
    print("Error! You need to enter a four-digit natural number")
else:
    temp = 1
    for i in num:
        temp *= int(i)
    print("The product of the digits of this number:", temp)
    print("The number in reverse order:", num[::-1])
    print("Numbers included in the given number, sorted in ascendic order:", "".join(sorted(num)))