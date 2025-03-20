import hw08_task3_mymod as m
    
choice = input("Area of which figure do you want to calculate? \n1 - rectangle \n2 - triangle \n3 - circle \nplease enter the number of your choice: ")
match choice:
    case "1":
        l = input("Enter length of rectangle:\t")
        w = input("Enter width of rectangle:\t")
        if m.is_positive_float(l) and m.is_positive_float(w):
            a = m.area_rectangle(float(l), float(w))
            print(f"The area of rectangle is:\t {round(a)}")
        else:
            print("Error! Values must be positive numbers!")        
    case "2":
        b = input("Enter base of triangle:\t")
        h = input("Enter height of triangle:\t")
        if m.is_positive_float(b) and m.is_positive_float(h):
            a = m.area_triangle(float(b), float(h))
            print(f"The area of triangle is:\t {round(a)}")
        else:
            print("Error! Values must be positive numbers!")
    case "3":
        r = input("Enter radius of a circle:\t")
        if m.is_positive_float(r):
            a = m.area_circle(float(r))
            print(f"The area of the circle is:\t {round(a,1)}")
        else:
            print("Error! Radius must be positive number!")
    case _:
        print("Error! Wrong choice of shape")