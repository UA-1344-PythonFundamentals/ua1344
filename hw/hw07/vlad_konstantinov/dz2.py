def area_rectangle(length, width):
    return length * width

def area_triangle(height, length):
    return (height * length) / 2

def area_circle(radius, pi):
    return (radius ** 2) * pi

print(f"Pick area search ")
st = input(f"Rectangle: 1 \n"
           f"Triangle:  2 \n"
           f"Circle:    3 \n"
           f"Your number: "
           )
try:
    st = int(st)
except ValueError:
    print("Invalid")
    exit()

match st:
    case 1:
        length = float(input("Length: "))
        width = float(input("Width: "))
        print(f"Rectangle area: {area_rectangle(length, width)}")

    case 2:
        height = float(input("Height: "))
        length = float(input("Base length: "))
        print(f"Triangle area: {area_triangle(height, length)}")

    case 3:
        radius = float(input("Radius: "))
        print(f"Circle area: {area_circle(radius)}")

    case _:
        print("Invalid choice! Please enter 1, 2, or 3.")