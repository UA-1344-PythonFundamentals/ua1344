#HW program that prompts the user to enter a temperature in Celsius and then converts it to Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
if celsius >= (-273.15):
    print(str(celsius),"\N{DEGREE SIGN}C is equivalent to ", round(fahrenheit,2), "\N{DEGREE SIGN}F", sep='')
else:
    print("Error: Temperature below absolute zero (-273.15\N{DEGREE SIGN}C)")