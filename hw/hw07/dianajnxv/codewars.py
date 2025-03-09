#Task 1 - Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
    
#Task 2 - Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

print(distance(1, 1, 2, 2)) 

#Task 3 - No yelling!
def filter_words(st):
    st = st.strip().lower()
    st = ' '.join(st.split())
    return st.capitalize()

print(filter_words('Hello world!'))  
print(filter_words('This    will    not    pass '))  
print(filter_words('Now this is a very exciting test!')) 

#Task 4 - Convert a Number to a String
def number_to_string(num):
    return str(num)

print(number_to_string(5))

#Task 5 - Reversing Words in a String
def reverse(st):
    word = st.split()
    return ' '.join(reversed(word))

#Task 6 - Reverse List Order
def reverse_list(l):
    rev = l[::-1]
    return rev

print(reverse_list([1, 2, 3, 4]))

#Task 7 - Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
            
    return total

print(solution(10))  

#Task 8 - Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    
    return max_distance >= distance_to_pump
    
print(zero_fuel(50, 25, 2))

#Task 9 - Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("Ronny"))

#Task 10 - Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
print(bool_to_word(True))

#Task 11 - Counting sheep
def count_sheeps(sheep):
    if sheep is None:
        return 0
    return sheep.count(True)

sheep_array = [True, True, False, True, False, True, True]
print(count_sheeps(sheep_array))  

#Task 12 - Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail

print(correct_tail("lion", "n"))  
print(correct_tail("elephant", "t"))
print(correct_tail("zebra", "a"))  
print(correct_tail("giraffe", "e"))
