import geometry

def main():
    print("Choose your figure:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Your figure (1/2/3): ")

    if choice == "1":
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print(f"Rectangle area: {geometry.rectangle_area(a,b)}")

    elif choice == "2":
        a = float(input("Enter the base of the triangle: "))
        b = float(input("Enter the height of the triangle: "))
        print(f"Triangle area: {geometry.triangle_area(a,b)}")

    elif choice == "3":
        r = float(input("Enter the radius of the circle: "))
        print(f"Circle area: {geometry.circle_area(r)}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()