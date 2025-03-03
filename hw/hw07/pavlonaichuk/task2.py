import math

def rectangleArea(length, width):
    return length * width

def triangleArea(base, height):
    return 0.5 * base * height

def circleArea(radius):
    return math.pi * radius ** 2

print("Choose the shape to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of the rectangle:", rectangleArea(length, width))
elif choice == "2":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of the triangle:", triangleArea(base, height))
elif choice == "3":
    radius = float(input("Enter radius: "))
    print("Area of the circle:", circleArea(radius))
else:
    print("Invalid choice")
