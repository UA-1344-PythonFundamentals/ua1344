#In the range from 1 to 10 determine:
#even numbers that are divisible by 2,
#odd numbers, which are divisible by 3,
#numbers that are not divisible by 2 and 3.

for num in range(1, 11):
  if num % 2 == 0:
      print(f"{num} is even and divisible by 2")
  elif num % 2 != 0 and num % 3 == 0:
      print(f"{num} is odd and divisible by 3")
  elif num % 2 != 0 and num % 3 != 0:
      print(f"{num} is not divisible by 2 and 3")
  






  
  