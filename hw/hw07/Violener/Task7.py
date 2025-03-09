#def max_num(a,b):
#    """ This function takes two numbers as input and returns the larger one.
#        It works with both integers and floating-point numbers.
#        If the numbers are equal, it returns either of them.
#    """
#    if a > b:
#        print("a > b")
#    else:
#        print("a < b")
#
#max_num(5,6)        
#
#
#def area_rectangle(length, width):
#    return length * width
#
#def area_triangle(height, length):
#    return (height * length) / 2
#
#def area_circle(radius, pi = 3.14):
#    return (radius ** 2) * pi
#
#def main():
#    print("Choose a shape to calculate the area:")
#    print("1. Rectangle")
#    print("2. Triangle")
#    print("3. Circle")
#
#    choice = int(input("Enter the shape number (1, 2, or 3): "))
#
#    if choice == 1:
#            length = float(input("Enter the length of the rectangle: "))
#            width = float(input("Enter the width of the rectangle: "))
#            area = area_rectangle(length, width)
#            print(f"The area of the rectangle is: {area}")
#
#    elif choice == 2:
#            height = float(input("Enter the height of the triangle: "))
#            length = float(input("Enter the length of the triangle: "))
#            area = area_triangle(height, length)
#            print(f"The area of the triangle is: {area}")
#
#    elif choice == 3:
#            radius = float(input("Enter the radius of the circle: "))
#            area = area_circle(radius, pi = 3.14)
#            print(f"The area of the circle is: {area}")
#
#    else:
#        print("Invalid choice, please select 1, 2, or 3.")
#
#main()



#def calculate_str(string):
#    symbol_count = {}
#    for i in string:
#            if i in symbol_count:
#                symbol_count[i] += 1
#            else:
#                symbol_count[i] = 1
#    print(symbol_count)
#
#
#
#calculate_str("Helloo World")  



#1
#def greet(name):
# 
#    if name == "Johnny":
#        return "Hello, my love!"
#    return f"Hello, {name}!"
#3
#def filter_words(sentence):
#     return sentence.capitalize()
#
#print(filter_words("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHello"))

#4 
#def convert(a):
#    print(type(a))
#    return str(a)
#print(type(convert(5)))

#5
def reverse_words(sentence):
    words = sentence.split()  
    reversed_words = reversed(words)  
    return " ".join(reversed_words)
#6
def reverse_list(lst):
   
    return lst[::-1]
#7
def sum_of_multiples(n):

    if n < 0:
        return 0  
    
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
#8
def can_reach_pump(distance_to_pump, mpg, fuel_left):

    return mpg * fuel_left >= distance_to_pump
#9
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    return f"{name} does not play banjo"
#10
def bool_to_word(boolean):

    return "Yes" if boolean else "No"
#11
def count_sheep(sheep_list):
    return sum(1 for sheep in sheep_list if sheep is True)
#12
def correct_tail(body, tail):
    return body[-1] == tail
