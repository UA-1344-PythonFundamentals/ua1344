# 1. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# 2. Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# 3. No yelling!
def filter_words(st):
    lst = st.split()
    return " ".join(lst).capitalize()


# 4. Convert a Number to a String!
def number_to_string(num):
    return str(num)


# 5. Reversing Words in a String
def reverse(st):
    lst_st = st.split()
    lst_st.reverse()
    return " ".join(lst_st)


# 6. Reverse List Order
def reverse_list(lst):
    """return a list with the reverse order of l"""
    return list(reversed(lst))


# 7. Multiples of 3 or 5
def solution(number):
    sum_number = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_number += i

    return sum_number


# 8. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    return False


# 9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# 10. Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# 11. Counting sheep...
def count_sheeps(sheep):
    # TODO May the force be with you
    return sheep.count(True)


# 12. Is this my tail?
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
