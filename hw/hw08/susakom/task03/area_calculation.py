# task 3
import math

def get_rectangle_area(a,b):
    rectangle_area=round(a*b,2)
    return  rectangle_area


def get_triangle_area(a, b, c):
    p=1/2*(a+b+c)
    triangle_area=round((p*(p-a)*(p-b)*(p-c))**0.5,2)
    return triangle_area



def get_circle_area(r):
    circle_area=round(math.pi*r**2,2)
    return circle_area

__all__ = ['get_rectangle_area', 'get_triangle_area', 'get_circle_area']