import math

# Calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Calculate the area of a circle
def area_of_circle(radius):
    return round(math.pi * math.pow(radius, 2), 2)
