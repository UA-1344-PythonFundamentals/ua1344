# 1. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

print("--------------------------------------")
print("Task 1. Jenny's secret message")
print(greet("Bill"))  # "Hello, Bill!"
print(greet("Johnny"))  # "Hello, my love!"
print("--------------------------------------")

# 2. Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

print("Task 2. Find The Distance Between Two Points")
print(distance(1, 1, 0, 0))  # 1.41
print(distance(1, 1, 2, 2))  # 1.41
print(distance(1, 1, 3, 3))  # 2.83
print("--------------------------------------")

# 3. No yelling!
def filter_words(st):
    words = st.split()
    words = [word.lower() for word in words]
    words[0] = words[0].capitalize()
    return " ".join(words)

print("Task 3. No yelling!")
print(filter_words("HELLO world!"))  # "Hello world!"
print(filter_words("TODAY is THE day!"))  # "Today is the day!"
print(filter_words("TODAY is THE very        loOOooOOooOOoong          day!"))  # "Today is the day!"
print("--------------------------------------")

# 4. Convert a Number to a String!
def number_to_string(num):
    return str(num)

print("Task 4. Convert a Number to a String!")
print(number_to_string(123))  # "123"
print(number_to_string(999))  # "999"
print(number_to_string(0))  # "0"
print("--------------------------------------")

# 5. Reversing Words in a String
def reverse(st):
    return " ".join(st.split()[::-1])

print("Task 5. Reversing Words in a String")
print(reverse("Hello World"))  # "World Hello"
print(reverse("a b c d"))  # "d c b a"
print("--------------------------------------")

# 6. Reverse List Order
def reverse_list(l):
    return l[::-1]

print("Task 6. Reverse List Order")
print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
print(reverse_list([3, 1, 5, 4]))  # [4, 5, 1, 3]
print(reverse_list([3, 6, 9, 12]))  # [12, 9, 6, 3]
print("--------------------------------------")

# 7. Multiples of 3 or 5
def solution(number):
    return 0 if number < 0 else sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print("Task 7. Multiples of 3 or 5")
print(solution(10))  # 23
print(solution(20))  # 78
print(solution(200))  # 9168
print(solution(-10))  # 0
print("--------------------------------------")

# 8. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

print("Task 8. Will you make it?")
print(zero_fuel(50, 25, 2))  # True
print(zero_fuel(100, 50, 1))  # False
print("--------------------------------------")

# 9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

print("Task 9. Are You Playing Banjo?")
print(are_you_playing_banjo("Roman"))  # "Rikke plays banjo"
print(are_you_playing_banjo("Martin"))  # "Martin does not play banjo"
print("--------------------------------------")

# 10. Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

print("Task 10. Convert boolean values to strings 'Yes' or 'No'.")
print(bool_to_word(True))  # "Yes"
print(bool_to_word(False))  # "No"
print("--------------------------------------")

# 11. Counting sheep...
def count_sheeps(sheep):
  return sum(1 for s in sheep if s)

sheep_list = [
    True, True, True, False,
    True, True, True, True,
    True, False, True, False,
    True, False, False, True,
    True, True, True, True,
    False, False, True, True
]

print("Task 11. Counting sheep...")
print(count_sheeps(sheep_list))  # 17
print("--------------------------------------")

# 12. Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail

print("Task 12. Is this my tail?")
print(correct_tail("Fox", "x"))  # True
print(correct_tail("Fox", "o"))  # False
print("--------------------------------------")
