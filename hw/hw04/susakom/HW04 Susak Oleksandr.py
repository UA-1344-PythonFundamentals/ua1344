# HW04 Susak Oleksandr
temperature =float(input("Enter the temperature in Celsius:"))
T_in_K = round(temperature+273.15, 2)
abs_zero= 0
if T_in_K > abs_zero:
    F_temperature = round((temperature * 9/5)+32, 2)
    print(f"{temperature} °C is equivalent to {F_temperature} °F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")