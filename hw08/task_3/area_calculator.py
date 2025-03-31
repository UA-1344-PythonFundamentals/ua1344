# area_calculator.py
import math

def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.
    Parameters:
    a (float): Length of the rectangle.
    b (float): Width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return a * b

def triangle_area(h, a):
    """
    Calculate the area of a triangle.
    Parameters:
    h (float): Height of the triangle.
    a (float): Base of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * h * a

def circle_area(r):
    """
    Calculate the area of a circle.
    Parameters:
    r (float): Radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return math.pi * math.pow(r, 2)
