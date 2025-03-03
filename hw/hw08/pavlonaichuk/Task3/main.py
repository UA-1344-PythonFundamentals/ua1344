from areaCalculations import rectangleArea, triangleArea, circleArea

def main():
    print("Choose the shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        a = float(input("Enter length: "))
        b = float(input("Enter width: "))
        print("Area of rectangle:", rectangleArea(a, b))
    elif choice == '2':
        h = float(input("Enter height: "))
        a = float(input("Enter base: "))
        print("Area of triangle:", triangleArea(h, a))
    elif choice == '3':
        r = float(input("Enter radius: "))
        print("Area of circle:", circleArea(r))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
