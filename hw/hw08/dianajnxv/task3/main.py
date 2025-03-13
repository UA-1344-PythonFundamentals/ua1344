import geometry

def choice():
    print("Chose a figure to calculate:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")

    figure = input("Enter the number of the figure: ")  
    if figure == "1":
        width = float(input("Enter width: "))  
        height = float(input("Enter height: "))
        print(geometry.rectangle(width, height))

    elif figure == "2":
        side = float(input("Enter side: "))
        height = float(input("Enter height: "))
        print(geometry.triangle(side, height))

    elif figure == "3":
        radius = float(input("Enter radius: "))
        print(geometry.circle(radius))

    else:
        print("Invalid choice, please enter 1, 2, or 3.")

if __name__ == "__main__":
    choice() 
