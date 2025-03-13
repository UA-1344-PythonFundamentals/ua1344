temp_c = float(input("Enter the temperature in Celsius: "))
if temp_c < -273.15:
    print("Error: Temperature below absolute zero (-273.15\N{DEGREE SIGN}C)")
else:
    temp_f = (temp_c * 9 / 5) + 32
    print(f"{round(temp_c)}\N{DEGREE SIGN}C is equivalent to {round(temp_f)}\N{DEGREE SIGN}F")