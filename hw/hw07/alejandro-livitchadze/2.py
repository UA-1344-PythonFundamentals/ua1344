def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

shape = input("Choose shape (rectangle/triangle/circle): ").strip().lower()

match shape:
    case "rectangle":
        w = float(input("Width: "))
        h = float(input("Height: "))
        print("Square:", rectangle_area(w, h))
    case "triangle":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Square:", triangle_area(b, h))
    case "circle":
        r = float(input("Radius: "))
        print("Square:", circle_area(r))
    case _:
        print("Unknown shape!")