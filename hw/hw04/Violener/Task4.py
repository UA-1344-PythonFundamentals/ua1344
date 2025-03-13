while True:
    try:
        celsius = (input("enter temperature in celsius:"))
        if celsius.lower() == "q":
                print("exit")
                break
        if float(celsius) < -273.15:
            print("the data was entered incorrectly")
        else:
            fahrenheit = ((float(celsius) * 9/5) + 32)
            print(f"{celsius} degrees Celsius equals {fahrenheit} degrees Fahrenheit")
    except ValueError:
        print("Error: Please enter a numeric value!")    