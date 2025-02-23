#1
list = [1,2,3,4,5,6,7,8,9]
floa_list = []

for i in list:
    floa_list.append(float(i))

print(f"{floa_list}")

#2
def fib(n):
    fib_sqe = []
    a, b = 0, 1
    for _ in range(n):
        fib_sqe.append(a)
        a, b = b, a + b
    return fib_sqe

print(fib(10))

#3
n = int(input())
factorial = 1

for i in range(1, n+1):
    factorial *= i

print(f"!{n} = {factorial}")