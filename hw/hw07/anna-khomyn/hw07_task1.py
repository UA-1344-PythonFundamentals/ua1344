def largest(a, b):
    """The function takes two numbers as arguments and returns larger of them.
    Note: type of input parameters must be int or float
    """
    if type(a) in (int, float) and type(b) in (int, float):
        return a if a > b else b
    else:
        print("Error! Parameters must be int or float")

print(help(largest))
print(largest(5, 7))
print(largest(23, -23))
print(largest(29.03, 29.05))
print(largest(15, "test"))