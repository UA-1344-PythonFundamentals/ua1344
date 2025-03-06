import math

def calculate_rectangle_area():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    return a*b

def calculate_triangle_area():
    a = int(input("enter a: "))
    h = int(input("enter h: "))
    return (a*h)/2

def calculate_circle_area():
    r = int(input("enter r: "))
    return round(math.pi*(pow(r,2)),2)

