from calcFunctions import *

def calc():
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    shape = input("Type number 1/2/3 to choose: ")

    if shape == "1":
        a = float(input("length of the rectangle: "))
        b = float(input("width of the rectangle: "))
        print(f"Rectangle area is: {areaRectangle(a,b)}")
    elif shape == "2":
        a = float(input("base of the triangle: "))
        h = float(input("height of the triangle: "))
        print(f"Triangle area is: {areaTriangle(a,h)}")
    elif shape == "3":
        r = float(input("radius of the circle: "))
        print(f"Circle area is: {areaCircle(r)}")
    else:
        print("Shape is not found.")

calc()