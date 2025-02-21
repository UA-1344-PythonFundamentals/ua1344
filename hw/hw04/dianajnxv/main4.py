user_input = float(input("Enter the temperature in Celsius: "))
f = (user_input * 9/5) + 32

if user_input >= -273.15:
    print(f"{user_input}°C is equivalent to {f}°F")
else: 
    print("Error: Temperature below absolute zero(-273.15)")
