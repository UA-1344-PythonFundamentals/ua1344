# Option 1
def largest_number_max(num1, num2):
    """ This function takes two numbers as input and returns the larger one.
        It works with both integers and floating-point numbers.
        If the numbers are equal, it returns either of them.
    """
    return max(num1, num2)

print(largest_number_max(4.6, 5))

# Option 2
def largest_number_if(num1, num2):
    """ This function takes two numbers as input and returns the larger one.
        It works with both integers and floating-point numbers.
        If the numbers are equal, it returns either of them.
    """
    if num1 > num2:
        return num1
    else:
        return num2

print(largest_number_if(25.89, 16))