#Task_01
def max_number(a,b):
    """
    
    Return the larger of two numbers.

    Parameters:
    a (int, float) - first number
    b (int, float) - second number
    
    Return:

    int or float - larger of the two numbers
    
    """
    return max(a, b)

#Task_02
def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

a = input("The area of ​what you need to know: ")

if a == "rectangle":
    length = int(input("Please enter a length of rectangle: "))
    width = int(input("Please enter a width of rectangle: "))
    print(f"The area of the rectangle is: {rectangle_area(length, width)}")

elif a == "triangle":
    base = float(input("Please enter a base of triangle: "))
    height = float(input("Please enter a height of triangle: "))
    print(f"The area of the triangle is: {triangle_area(base, height)}")

elif a == "circle":
    radius = float(input("Please enter a radius of circle: "))
    print(f"The area of the circle is: {circle_area(radius)}")

#Task_03
def count_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count