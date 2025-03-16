def largest_number(num1, num2):
    """
    This function takes two numbers as input and returns the larger of the two.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.

    Returns:
    int or float: The larger of the two input numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2

# Запит користувача для введення двох чисел
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Виклик функції з введеними числами
result = largest_number(num1, num2)

# Виведення результату
print("The largest number is:", result)
