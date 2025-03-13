#task_1
list = [1,2,3,4,5,6,7,8,9]
f_list = []

for num in list:
    f_list.append(float(num))

print(f_list)

#task_2
n = int(input())
a, b = 0, 1

while a <=n:
    print(a, end=" ")
    a, b = b, a+b

#task_3
n = int(input())
factorial = 1

for i in range(1, n+1):
    factorial *= i

print(f"!{n} = {factorial}")