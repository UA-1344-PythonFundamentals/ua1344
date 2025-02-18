tempC = float(input("Enter the temperature in Celsius: "))
abs_zero = - 273.15
if tempC > abs_zero:
    tempF = int(((tempC *9/5) + 32))
    print(f"{tempC}°C is equivalent to {tempF}°F")
else:
    print(f"Error: Temperature below absolute zero (-273.15 °C)")
