number = int(input("Enter a number: "))

a = 0
b = 1
while a <= number:
    print(a, end=" ")
    a , b = b, a + b  