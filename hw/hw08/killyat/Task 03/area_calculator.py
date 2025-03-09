import math

def area_rectangle(a, b):
    """Calculates the area of a rectangle: S = a * b."""
    return a * b

def area_triangle(h, a):
    """Calculates the area of a triangle: S = 0.5 * h * a."""
    return 0.5 * h * a

def area_circle(r):
    """Calculates the area of a circle: S = pi * r^2."""
    return math.pi * math.pow(r, 2)