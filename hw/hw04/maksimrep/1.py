# ask user to input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Check if the input is below absolute zero
if celsius >= -273.15:
    # Convert Celsius to Fahrenheit
    far = (celsius * 9/5) + 32
    print(f"{celsius}°C is equivalent to {far}°F")
else:
    print(f"Error: Temperature is below absolute zero  (-273,15°C)")
