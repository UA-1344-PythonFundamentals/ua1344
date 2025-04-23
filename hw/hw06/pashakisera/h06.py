# task1
int_list = [1, 2, 3, 4, 5]
float_list = [float(num) for num in int_list]
print(float_list)

# task2
while True:
  n = int(input("enter num: "))
  fib_list = [0, 1]
  while fib_list[-1] + fib_list[-2] <= n:
      fib_list.append(fib_list[-1] + fib_list[-2])
  print( fib_list)
  if n== "q":
     break

# task3
num = int(input("enter num: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! =", factorial)