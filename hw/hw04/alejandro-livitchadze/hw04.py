def fahrenheit_to_celsius ():
    ABSOLUTE_ZERO = -273.15
    celsius = float(input("Enter the temperature in Celcius: "))
    if celsius < ABSOLUTE_ZERO:
        print("The temperature is below absolute zero. Please enter a valid temperature.")
        fahrenheit_to_celsius()
    else:
        fahrenheit = celsius * 9/5 + 32
        print(f"The temperature in Fahrenheit is {fahrenheit:.2f}")

fahrenheit_to_celsius()