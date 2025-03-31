#Write a script that will calculate the factorial of the entered number without using recursion
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")


  
  