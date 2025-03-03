def largest_num (a, b):
    """This funktion return
    the largest number"""
    if a > b:
        print(a)
    else:
        print(b)

largest_num(9, 3)
print(largest_num.__doc__)

def area_rectangle (a, b):
    return a * b
print("Area of a rectangle: ", area_rectangle(3, 8))

def area_triangle (c, h):
    return c * h
print("Area of a triangle: ", area_triangle(4, 9))

def area_circle (r, TT = 3.14):
    return (r**2)*TT
print("Area of a circle: ", area_circle(6))


def count_letters(greeting):
    count = 0
    for letter in greeting:
        count += 1
        print(letter,":",count)

user_input = input("Введіть вітання: ")
count_letters(user_input)
