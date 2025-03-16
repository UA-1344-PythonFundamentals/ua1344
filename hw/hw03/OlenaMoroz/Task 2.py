number = 1992
#find the product of the digits
product = 1
for digit in str(number):
  product *= int(digit)
  print(f"Product of digits: {product}")

#write the number in reverse order
reversed_number = int(str(number)[::-1])
print(f"Reversed number: {reversed_number}")

#in ascending order you need to sort the numbers included in the given number
sorted_number = "".join(sorted(str(number)))
print(f"Sorted number in ascending order: {sorted_number}")



  


  






















