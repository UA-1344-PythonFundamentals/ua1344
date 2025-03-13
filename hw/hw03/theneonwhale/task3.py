def interchange_values():
    a = input("Enter value for a: ")
    b = input("Enter value for b: ")

    print(f"Before interchange: a = {a}, b = {b}")

    # Interchange using tuple unpacking
    a, b = b, a

    # Interchange using list
    # a, b = [b, a]

    # Interchange using addition and subtraction if a and b are numbers
    # a = int(a)
    # b = int(b)
    # a = a + b
    # b = a - b
    # a = a - b

    print(f"After interchange: a = {a}, b = {b}")

interchange_values()
