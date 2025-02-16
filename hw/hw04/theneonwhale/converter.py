def temperature_converter():
    ABSOLUTE_ZERO = -273.15

    celsius = float(input("Enter the temperature in Celsius: "))

    if celsius < ABSOLUTE_ZERO:
        print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO}°C)")
    else:
        fahrenheit = round((celsius * 9/5) + 32, 2)
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")

temperature_converter()
