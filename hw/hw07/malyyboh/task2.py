def calculate_area_rectangle(L, w):
    return f"Area of rectangle: {L * w}"


def calculate_area_triangle(b, h):
    return f"Area of triangle: {0.5 * b * h}"


def calculate_area_circle(r, p=3.14):
    return f"Area of circle: {p * r**2}"


user_input = input(
    "Program for calculating the area of figures. \nto calculate the area of a rectangle, enter: rectangle \nto calculate the area of a triangle, enter: triangle \nto calculate the area of a circle, enter: circle \nPlease enter the figure: "
)

if user_input == "rectangle":
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print(calculate_area_rectangle(length, width))
elif user_input == "triangle":
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    print(calculate_area_triangle(base, height))
elif user_input == "circle":
    radius = int(input("Enter the radius: "))
    print(calculate_area_circle(radius))
