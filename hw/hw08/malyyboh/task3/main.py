import func_module
from math import pi, pow

user_input = input(
    "Program for calculating the area of figures. \nto calculate the area of a rectangle, enter: rectangle \nto calculate the area of a triangle, enter: triangle \nto calculate the area of a circle, enter: circle \nPlease enter the figure: "
)

if user_input == "rectangle":
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print(func_module.calculate_area_rectangle(length, width))
elif user_input == "triangle":
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    print(func_module.calculate_area_triangle(base, height))
elif user_input == "circle":
    radius = int(input("Enter the radius: "))
    pow_r = pow(radius, 2)
    print(func_module.calculate_area_circle(radius, pi, pow_r))
