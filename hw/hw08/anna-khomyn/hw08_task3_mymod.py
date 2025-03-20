from math import pi, pow

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return base * height / 2

def area_circle(radius):
    return pi * pow(radius, 2)

def is_positive_float(str):
    """The function checks if the string value is positive number"""

    if str.replace('.','').isdigit():
        return True
    else:
        return False