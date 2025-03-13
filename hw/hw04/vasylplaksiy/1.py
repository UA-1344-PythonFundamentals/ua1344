inputCelsius = float(input("Enter the temperature in Celsius: "))
ABSOLUTE_ZERO_C = -273.15
if inputCelsius < ABSOLUTE_ZERO_C:
    print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO_C}°C)")
else:
    convertedToFahrenheit = inputCelsius * 9 / 5 + 32
    print(f"{str(inputCelsius).replace('.0', '')}°C is equivalent to {str(round(convertedToFahrenheit, 2)).replace('.0', '')}°F")