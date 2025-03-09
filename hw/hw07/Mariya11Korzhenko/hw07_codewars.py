def greet(name):
    """Jenny's secret message
    """
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def distance(x1, y1, x2, y2):
    """Simple: Find The Distance Between Two Points
    """
    return round(((x2-x1)**2+(y2-y1)**2)** .5, 2)


def filter_words(st):
    """No yelling!"""
    capitalized_string = st.capitalize()
    return " ".join(capitalized_string.split())


def number_to_string(num):
    """Convert a Number to a String"""
    num_to_str = num
    return str(num_to_str)


def reverse(st):
    """Reversing Words in a String"""
    result = []
    original_order = st.split()
    for i in range(len(original_order), 0, -1):
        print(i)
        result.append(original_order[i-1])
    return " ".join(result)


def reverse_list(l):
    """Reverse List Order"""
    result = []
    for i in range(len(l), 0, -1):
        result.append(l[i-1])
    return result
    

def reverse_list(l):
    """Reverse List Order (simple impl)"""
    return l[::-1]


def solution(number):
    """Multiples of 3 or 5"""
    result = 0
    i = 0
    while i<number:
        if (i%3 == 0 or i%5 == 0):
            if( i<number):
                result = result + i
            else:
                break
        i = i + 1 

    return result

def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Will you make it?"""
    return fuel_left >= distance_to_pump  /mpg


def are_you_playing_banjo(name):
    """Are You Playing Banjo?"""
    if(name[0] == 'R' or name[0] == 'r'):
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"


def count_sheeps(sheep):
    """Counting sheep..."""
    result = 0
    for i in sheep:
        if i:
            result +=1
            
    return result

def correct_tail(body, tail):
    """Is this my tail?"""
    return body[-1] == tail

# correct_tail = lambda a,t: a[-1]==t

