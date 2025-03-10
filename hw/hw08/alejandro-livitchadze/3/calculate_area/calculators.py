from math import pow, pi

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return pow(base * height, 0.5)

def circle_area(radius):
    return pow(pi * radius, 2)