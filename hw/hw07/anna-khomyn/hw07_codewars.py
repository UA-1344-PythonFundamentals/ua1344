# ==========    1   ==========
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# ==========    2   ==========

def distance(x1, y1, x2, y2):
    res = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(res, 2)

# ==========    3   ==========

def filter_words(st):
    st = st.split()
    st = " ".join(st)
    return st.capitalize()
#print (filter_words('This    will    not    pass '))

# ==========    4   ==========

def number_to_string(num):
    return str(num)

# ==========    5   ==========

def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    return st
#print(reverse('Hello World'))

# ==========    6   ==========

def reverse_list(l):
    l.reverse()
    return l
#print(reverse_list([1,2,3,4]))

# ==========    7   ==========

def solution(number):
    if number < 0:
        return 0
    res = []
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            res.append(n)
    return sum(res)
#print(solution(6))


# ==========    8   ==========

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False

# ==========    9   ==========

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return "{} plays banjo".format(name)
    else:
        return "{} does not play banjo".format(name)
#print(are_you_playing_banjo("Robert"))

# ==========    10   ==========

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# ==========    11   ==========

def count_sheeps(sheep):
    return sheep.count(True)

# ==========    12   ==========

def correct_tail(body, tail):
    return True if body[-1] == tail else False
