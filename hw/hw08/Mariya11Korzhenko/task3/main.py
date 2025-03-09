from area import *

def choose_area_base():
    """function calculates the area of figure"""
    area_base = input("Choose are base (triangle|rectangle|circle): ")
    result = 0
    match area_base:
        case "triangle": result = calculate_triangle_area()
        case "rectangle": result = calculate_rectangle_area()
        case "circle": result = calculate_circle_area()
        case _: 
            print("Area base is unknown: " + area_base)

    return result

print(choose_area_base())