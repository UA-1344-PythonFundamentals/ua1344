def largest_number(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): first number.
    b (int or float): second number.

    Returns:
    int or float: largest number.
    """
    return a if a > b else b

print(largest_number.__doc__)
print(largest_number(5, 10))  # 10
print(largest_number(15, 10))  # 15
print(largest_number(5.3, 5.1))  # 5.3
print(largest_number(5, 4.9))  # 5
