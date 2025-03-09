import area_of_figures

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    try:
        choice = int(input("Enter the shape number (1, 2, or 3): "))

        if choice == 1:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = area_of_figures.area_rectangle(length, width)
            print(f"The area of the rectangle is: {area:.2f}")

        elif choice == 2:
            height = float(input("Enter the height of the triangle: "))
            length = float(input("Enter the length of the triangle: "))
            area = area_of_figures.area_triangle(height, length)
            print(f"The area of the triangle is: {area:.2f}")

        elif choice == 3:
            radius = float(input("Enter the radius of the circle: "))
            area = area_of_figures.area_circle(radius)
            print(f"The area of the circle is: {area:.2f}")

        else:
            print("Invalid choice, please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()