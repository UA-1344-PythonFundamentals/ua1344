def area_rectangle():
    """The function asks the user to enter length and width of a rectangle, 
    checks if entered values are positive numbers and calculates the area of rectangle
    by formula:
            area = length * width
    """

    l = input("Enter length of rectangle:\t")
    w = input("Enter width of rectangle:\t")
    if is_positive_float(l) and is_positive_float(w):
        a = round(float(l) * float(w), 1)
        print(f"The area of rectangle is:\t {a}")
        return a
    else:
        print("Error! Values must be positive numbers!")

def area_triangle():
    """The function asks the user to enter base and height of a triangle, 
    checks if entered values are positive numbers and calculates the area of triangle
    by formula:
            area = base * height / 2
    """

    b = input("Enter base of triangle:\t")
    h = input("Enter height of triangle:\t")
    if is_positive_float(b) and is_positive_float(h):
        a =  round(float(b) * float(h) / 2, 1)
        print(f"The area of triangle is:\t {a}")
        return a
    else:
        print("Error! Values must be positive numbers!")

def area_circle():
    """The function asks the user to enter radius of a circle, 
    checks if entered value is positive number and calculates the area of circle
    by formula:
            area = PI * radius * radius
    """

    r = input("Enter radius of a circle:\t")
    if is_positive_float(r):
        PI = 3.1415
        a = round(PI * float(r) ** 2, 1)
        print(f"The area of the circle is:\t {a}")
        return a
    else:
        print("Error! Radius must be positive number!")

def is_positive_float(str):
    """The function checks if the string value is positive number"""

    if str.replace('.','').isdigit():
        return True
    else:
        return False
    

choice = input("Area of which figure do you want to calculate? \n1 - rectangle \n2 - triangle \n3 - circle \nplease enter the number of your choice: ")
match choice:
    case "1":
        area_rectangle()
    case "2":
        area_triangle()
    case "3":
        area_circle()
    case _:
        print("Error! Wrong choice of shape")