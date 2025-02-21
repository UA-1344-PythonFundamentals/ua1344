# user to enter a temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Check if the temperature is below absolute zero
if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15C)")
else:
    # Convert Celsius to Fahrenheit using the formula F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    # Print the result 
    print(f"{celsius}C is equivalent to {fahrenheit}F")
