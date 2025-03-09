from utils import *
from models import *

#print(list(filter(lambda str: not ("__" in str), dir())))


#is_valid_password("123456")

print("Choose a shape to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
choice = int(input("Enter the shape number (1, 2, or 3): "))
if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
elif choice == 2:
        height = float(input("Enter the height of the triangle: "))
        length = float(input("Enter the length of the triangle: "))
        area = triangle_area(height, length)
        print(f"The area of the triangle is: {area}")
elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius, pi = 3.14)
        print(f"The area of the circle is: {area}")
else:
    print("Invalid choice, please select 1, 2, or 3.")