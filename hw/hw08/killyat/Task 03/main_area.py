from area_calculator import *

if __name__ == "__main__":
    print("Choose a figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        a = float(input("Enter length (a): "))
        b = float(input("Enter width (b): "))
        print(f"Area of rectangle: {area_rectangle(a, b)}")
    elif choice == 2:
        h = float(input("Enter height (h): "))
        a = float(input("Enter base (a): "))
        print(f"Area of triangle: {area_triangle(h, a)}")
    elif choice == 3:
        r = float(input("Enter radius (r): "))
        print(f"Area of circle: {area_circle(r)}")
    else:
        print("Invalid choice!")