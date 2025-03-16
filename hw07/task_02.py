import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    """
    This function calculates the area of a rectangle.
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Function to calculate the area of a triangle
def triangle_area(base, height):
    """
    This function calculates the area of a triangle.
    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

# Function to calculate the area of a circle
def circle_area(radius):
    """
    This function calculates the area of a circle.
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2

# Main program
print("Choose the shape to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = input("Enter the number corresponding to the shape: ")

if choice == '1':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")

elif choice == '2':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area}")

elif choice == '3':
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area}")

else:
    print("Invalid choice! Please enter a valid number.")
