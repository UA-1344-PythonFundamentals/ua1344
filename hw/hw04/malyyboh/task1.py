user_input_temp = float(input("Please enter the temperature in Celsius: "))

if user_input_temp > (-273.15):
    temp_in_fahrenheit = (user_input_temp * 9 / 5) + 32
    print(f"Enter the temperature in Celsius: {user_input_temp}")
    print(f"{user_input_temp}°C is equivalent to {temp_in_fahrenheit}°F")
else:
    print(f"Enter the temperature in Celsius: {user_input_temp}")
    print("Error: Temperature below absolute zero (-273.15°C)")
