# 1. Jenny's Greeting Function
def greet(name):
    if name.lower() == "johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# Testing
print("Task 1:")
print(greet("Johnny"))  # Expected: "Hello, my love!"
print(greet("Jenny"))   # Expected: "Hello, Jenny!"
print("-" * 50)

# 2. Calculate Distance Between Two Points
def distance(x1, y1, x2, y2):
    from math import sqrt
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)

# Testing
print("Task 2:")
print(distance(0, 0, 3, 4))  # Expected: 5.0
print("-" * 50)

# 3. Capitalize and Proper Spacing
def filter_words(text):
    words = text.split()
    if words:
        words[0] = words[0].capitalize()
    for i in range(1, len(words)):
        words[i] = words[i].lower()
    return " ".join(words)

# Testing
print("Task 3:")
print(filter_words('HELLO CAN YOU HEAR ME'))  # Expected: "Hello can you hear me"
print(filter_words('now THIS is REALLY interesting'))  # Expected: "Now this is really interesting"
print(filter_words('THAT was EXTRAORDINARY!'))  # Expected: "That was extraordinary!"
print("-" * 50)

# 4. Transform Number to String
def number_to_string(num):
    return str(num)

# Testing
print("Task 4:")
print(number_to_string(123))  # Expected: "123"
print(number_to_string(999))  # Expected: "999"
print(number_to_string(-100)) # Expected: "-100"
print("-" * 50)

# 5. Reverse Words in a String
def reverse_words(text):
    words = ' '.join(text.split())
    return ' '.join(reversed(words.split()))

# Testing
print("Task 5:")
print(reverse_words("Hello World"))  # Expected: "World Hello"
print(reverse_words("Hi There."))    # Expected: "There. Hi"
print(reverse_words("Happy coding! ")) # Expected: "coding! Happy"
print("-" * 50)

# 6. Reverse a List
def reverse_list(lst):
    return lst[::-1]

# Testing
print("Task 6:")
print(reverse_list([1, 2, 3, 4]))  # Expected: [4, 3, 2, 1]
print(reverse_list([9, 2, 0, 7]))  # Expected: [7, 0, 2, 9]
print("-" * 50)

# 7. Sum of Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Testing
print("Task 7:")
print(solution(10))  # Expected: 23 (3 + 5 + 6 + 9)
print(solution(-1))  # Expected: 0
print("-" * 50)

# 8. Check if Car Can Reach Pump
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

# Testing
print("Task 8:")
print(zero_fuel(50, 25, 2))  # Expected: True (2 * 25 = 50 >= 50)
print(zero_fuel(100, 50, 1)) # Expected: False (1 * 50 = 50 < 100)
print("-" * 50)

# 9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"

# Testing
print("Task 9:")
print(are_you_playing_banjo("Robert"))  # Expected: "Robert plays banjo"
print(are_you_playing_banjo("Jenny"))   # Expected: "Jenny does not play banjo"
print("-" * 50)

# 10. Yes or No
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Testing
print("Task 10:")
print(bool_to_word(True))  # Expected: "Yes"
print(bool_to_word(False)) # Expected: "No"
print("-" * 50)

# 11. Count Sheep
def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

# Testing
array1 = [True, True, True, False, True, True, True, True, True, False, True, False,
          True, False, False, True, True, True, True, True, False, False, True, True]
print("Task 11:")
print(count_sheeps(array1))  # Expected: 17
print("-" * 50)

# 12. Correct Tail
def correct_tail(body, tail):
    return body[-1] == tail

# Testing
print("Task 12:")
print(correct_tail("Fox", "x"))      # Expected: True
print(correct_tail("Rhino", "o"))    # Expected: True
print(correct_tail("Emu", "t"))      # Expected: False
print("-" * 50)