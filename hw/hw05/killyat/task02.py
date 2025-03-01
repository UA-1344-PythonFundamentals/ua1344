n = int(input("Enter number n: "))
a, b = 0, 1
if n >= 0:
    print(a, end=" ")
while b <= n:
    print(b, end=" ")
    a, b = b, a + b