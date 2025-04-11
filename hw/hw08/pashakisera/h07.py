#Write a function that returns the largest number of two numbers
#(use DocStrings documentation strings in the function).

def compare(a,d):
    """The function compares two numbers, defines the biggest one and returns it"""
    return a if a >= d else d

print(compare(6,5))

# Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area.
# And call them in the main program depending on the user's choice).
#
# area = a*b
# triangle = 0.5*a*h
# circle = pi*r**2

import math


def area(figure, a, b=math.pi):
    """The function calculates the area of the selected figure with entered params and return it"""
    if figure == "rectangle":
        return a * b
    elif figure == "triangle":
        return 0.5 * a * b
    elif figure == "circle":
        return b * a ** 2


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

#Write a function that calculates the number of characters included in given string
#• input: "hello"
#• output: {"h":1, "e": 1, "I":2,"0":1}

def count_str(str_to_calc):
    res = {}
    for i in set(str_to_calc):
        res[i] = str_to_calc.count(i)
    print(res)

count_str("hello")
count_str("Python is awesome")