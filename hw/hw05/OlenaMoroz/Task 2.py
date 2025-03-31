#Print Fibonacci numbers up to the entered number n, using cycles
n = int(input("Enter a number: "))
a, b = 0, 1  
while a <= n:
  print(a, end=" ")
  a, b = b, a + b



  
  