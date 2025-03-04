#H08 task 03 Susak Oleksandr

from area_calculation import get_circle_area, get_rectangle_area, get_triangle_area



print("What do you what to callculate ?")
print("Enter you choice")
print("Please select 1 for rectangle, 2 for triangle, 3 for circle")
choice=int(input("You choice is "))
if choice == 1:
    a, b=input("Enter the sides of the rectangle separated by commas a, b) ").split(",")
    a=int(a)
    b=int(b)
    res=get_rectangle_area(a,b)
    print("Rectangle area=", res)
elif choice == 2:
    a, b, c=input("Enter the sides of the tirange separated by commas a, b, c) ").split(",")
    a=int(a)
    b=int(b)
    c=int(c)
    res=get_triangle_area(a,b,c)
    print("Triangle area=", res)
elif choice == 3:
    r=input("Enter the radius of the circle ")
    r=int(r)
    res=get_circle_area(r)
    print("Circle area=", res)
else:
    print("You entered wrong choice")
