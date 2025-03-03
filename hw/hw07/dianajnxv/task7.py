#Task 1
def large_numbers(num1, num2):
    """ 
    Function returns the larger of two given numbers.
    It works with both integers and floating-point numbers.
    If the numbers are equal, it returns either of them.
    
    """
    return max(num1, num2)

result = large_numbers(20, 30)
result2 = large_numbers(0.5, 0.1)
result3 = large_numbers(77, 77)

print(result)
print(result2)
print(result3)


#Task 2
import math 

def rectangle(width, height):
    area = width * height
    print("The area of rectangle is: ", area)

def triangle(side):
    area = math.sqrt(3)/4 * side ** 2
    print("The area of triangle is: ", area)

def circle(radius):
    area = math.pi * radius ** 2
    print("The area of circle is: ", area)

result_figures = input("Chose a figure: rectangle, triangle or circle: ")

if result_figures == "rectangle":
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    rectangle(width, height)
    
elif result_figures == "triangle":
    side = int(input("Enter side: "))
    triangle(side)
    
elif result_figures == "circle":
    radius = int(input("Enter radius: "))
    circle(radius)
    
else:
    print("There is no such figure")
    
    
#Task 3
def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_text = input("Enter a string: ")

result = count_characters(input_text)
print(result)
