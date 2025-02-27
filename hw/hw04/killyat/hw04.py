temperatureC = float(input("Enter temperature in Celsius:"))
temperatureF = (temperatureC * 9/5) +32

if temperatureC >= -273.15:
    print("Equivalent", temperatureF, "to Fahrenheit")
else:
    print("Error: Temperature below absolute zero")