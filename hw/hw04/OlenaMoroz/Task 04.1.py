#Program that converts Celsius to Farenheit
C = float(input("Enter temperature in Celsius: "))
F = (C * 9/5) + 32
if C>-273.15:
 print("The temperature in Fahrenheit is", F)
else:
  print("Error: Temperature is below absolute zero")
