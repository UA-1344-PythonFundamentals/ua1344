from modulemath import rectangle_func, triangle_func, circle_func

def main():
    print("Chose a figure to calculate:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    chose = input("Enter a number: ")
    if chose == "1":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(rectangle_func(width, height))

    elif chose == "2":
        a = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(triangle_func(a, height))

    elif chose == "3":
        radius = float(input("Enter radius: "))
        print(circle_func(radius))

    else:
        print("You dont pick a correct choice")

if __name__ == "__main__":
    main()