temperature_celsius = float(input("Enter temperature in Celsius: "))

if temperature_celsius < -273.15:
    print("Error: Temperature is below absolute zero (-273.15ºC)")
else:
    temperature_fahrenheit = (temperature_celsius*9/5) + 32
    print(f"{temperature_celsius:.2f}ºC is equivalent to {temperature_fahrenheit:.2f}ºF")

