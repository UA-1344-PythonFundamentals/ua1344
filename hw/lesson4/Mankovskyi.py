celsius = float(input("Enter the temperature using Celsius scale: "))
fahrenheit = (celsius * 9/5) + 32

if celsius >= -273.15:
    print(f"{celsius}°C is equal {fahrenheit}°F")
else:
    print("Temperature is below the absolute zero")
