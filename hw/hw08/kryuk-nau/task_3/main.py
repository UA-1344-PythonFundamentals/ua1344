# main.py
import area_calculator

def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter the number corresponding to the figure: ")

    if choice == '1':
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = area_calculator.rectangle_area(a, b)
        print(f"The area of the rectangle is: {area}")

    elif choice == '2':
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base of the triangle: "))
        area = area_calculator.triangle_area(h, a)
        print(f"The area of the triangle is: {area}")

    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        area = area_calculator.circle_area(r)
        print(f"The area of the circle is: {area}")

    else:
        print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
