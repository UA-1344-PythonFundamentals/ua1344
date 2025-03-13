def area_rectangle(length, width):
    """Calculates the area of a rectangle."""
    return length * width

def area_triangle(base, height):
    """Calculates the area of a triangle."""
    return 0.5 * base * height

def area_circle(radius):
    """Calculates the area of a circle (using π ≈ 3.14159)."""
    return 3.14159 * radius * radius

print("Choose a shape to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print(f"Area of rectangle: {area_rectangle(length, width)}")
elif choice == 2:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    print(f"Area of triangle: {area_triangle(base, height)}")
elif choice == 3:
    radius = float(input("Enter radius of circle: "))
    print(f"Area of circle: {area_circle(radius)}")
else:
    print("Invalid choice!")