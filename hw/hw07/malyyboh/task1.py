def get_largest_number(a, b):
    """
    Take two numbers and return the largest number.

    Args:
    a (int, float): first number.
    b (int, float): second number.

    Returns:
    int, float: The largest number.
    str: If the numbers are the same.
    """
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "The numbers are the same."


print(get_largest_number(2, 3))
print(get_largest_number(4.5, 1.5))
print(get_largest_number(2, 2))
