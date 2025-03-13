#Print Fibonacci numbers up to the entered number n, using cycles.
n = input('Please enter a number for Fibonacci numbers: ')
list = [0,1]
for i in range(int(n)):
    list.append(list[-1] + list[-2])

print(list)
