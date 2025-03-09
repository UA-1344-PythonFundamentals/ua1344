# Task3
# Write a program that calculates the area of a rectangle S=a*b, the area of a triangle S=0.5*h*a, 
# the area of a circle S=pi*r**2. This module must be used in another module in which we ask the user 
# the area of which figure he wants to calculate.
#
# (To perform the task, you need to import the math module, and from it the pow() 
# function and the value of the variable pi, and module, which contains three functions 
# for finding areas, into the main program. The basic logic of the program is executed in the main

import functions

def read_inputs():
    """The function gets data from CLI and call the 'area' function to calculate an area"""
    entered_figure = input("Please enter a figure (available values 'rectangle', 'triangle' and 'circle'): ")
    if entered_figure == "rectangle":
        entered_length = float(input("Please enter length: "))
        entered_width = float(input("Please enter width: "))
        print(functions.rectangle(entered_length, entered_width))
    if entered_figure == "triangle":
        entered_height = float(input("Please enter height: "))
        entered_base = float(input("Please enter base: "))
        print(functions.triangle(entered_height, entered_base))
    if entered_figure == "circle":
        entered_radius = float(input("Please enter radius: "))
        print(functions.circle(entered_radius))

if __name__ == "__main__":
    read_inputs()