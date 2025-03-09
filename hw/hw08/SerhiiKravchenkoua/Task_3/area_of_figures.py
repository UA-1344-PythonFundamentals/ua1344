import math


def area_rectangle(length, width):
    return length * width

def area_triangle(height, length):
    return (height * length) / 2

def area_circle(radius):
    return math.pi * math.pow(radius, 2)
