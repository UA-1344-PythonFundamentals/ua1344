import math

def largest_number(number1, number2):
    """
    function returns the largest number of two numbers
    """
    return number1 if number1 > number2 else number2


def area_of_triangle():
    """function calculates the area of triangle"""
    base = int(input("enter base: "))
    high = int(input("enter high: "))
    return 1 / 2 * base * high

def area_of_rectangle():
    """function calculates the area of rectangle"""
    length = int(input("enter length: "))
    width = int(input("enter width: "))

    return length * width

def area_of_circle():
    """function calculates the area of circle"""
    r = int(input("enter radius: "))

    return round(math.pi * (r **2), 2)

def choose_area_base():
    """function calculates the area of figure"""
    area_base = input("Choose are base (triangle|rectangle|circle): ")
    result = 0
    match area_base:
        case "triangle": result = area_of_triangle()
        case "rectangle": result = area_of_rectangle()
        case "circle": result = area_of_circle()
        case _: 
            print("Area base is unknown: " + area_base)

    return result

# print(choose_area_base())


def calculate_number_of_char(string):
    """function returns a dictionary with combination:  key = letter, value  = letter count in input string """
    result = dict()
    for i in string: result[i] = result[i] + 1 if i in result else 1

    return result

print(calculate_number_of_char("Hello"))









