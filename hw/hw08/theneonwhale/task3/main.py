import area

def main():
    print("Choose the shape to calculate the area:")
    print("1 for Rectangle")
    print("2 for Triangle")
    print("3 for Circle")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Rectangle area is: {area.area_of_rectangle(length, width)}")

    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Triangle area is: {area.area_of_triangle(base, height)}")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        print(f"Circle area is: {area.area_of_circle(radius)}")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

main()
