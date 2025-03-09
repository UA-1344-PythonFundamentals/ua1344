def find_largest(num1, num2):
    """
    Returns the largest number between two given numbers.
    
    Args:
        num1 (int/float): The first number to compare.
        num2 (int/float): The second number to compare.
    
    Returns:
        int/float: The larger of the two numbers.
    
    Example:
        >>> find_largest(5, 8)
        8
        >>> find_largest(3.5, 2.1)
        3.5
    """
    if num1 > num2:
        return num1
    else:
        return num2

print(find_largest(5, 8))
print(find_largest(3.5, 2.1))