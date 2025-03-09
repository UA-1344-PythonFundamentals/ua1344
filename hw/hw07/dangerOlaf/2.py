#Write a program that calculates the area of a rectangle, triangle and circle 
#(write three functions to calculate the area. 
#And call them in the main program depending on the user's choice).
#
# area = a*b
# triangle = 0.5*a*h
# circle = pi*r**2

import math

def area(figure, a, b = math.pi):
    """The function calculates the area of the selected figure with entered params and return it"""
    if figure == "rectangle":
        return a*b
    elif figure == "triangle":
        return 0.5*a*b
    elif figure == "circle":
        return b*a**2
    

def read_inputs():
    """The function gets data from CLI and call the 'area' function to calculate an area"""
    intered_figure = input("Please enter a figure (available values 'rectangle', 'triangle' and 'circle'): ")
    if intered_figure == "rectangle":
        intered_length = float(input("Please enter length: "))
        intered_width = float(input("Please enter width: "))
        print(area(intered_figure, intered_length, intered_width))
    if intered_figure == "triangle":
        intered_height = float(input("Please enter height: "))
        intered_base = float(input("Please enter base: "))
        print(area(intered_figure, intered_height, intered_base))
    if intered_figure == "circle":
        intered_radius = float(input("Please enter radius: "))
        print(area(intered_figure, intered_radius))

read_inputs()