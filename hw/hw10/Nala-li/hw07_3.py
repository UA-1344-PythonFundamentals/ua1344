def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dist, 2)


def filter_words(sentence):
    words = sentence.split()
    result = " ".join(words).capitalize()
    return result


def number_to_string(n):
    return str(n)


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


def reverse_list(lst):
    return lst[::-1]


def solution(n):
    if n < 0:
        return 0
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)


def can_reach_pump(distance_to_pump, miles_per_gallon, fuel_left):
    return fuel_left * miles_per_gallon >= distance_to_pump


def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    return name + " does not play banjo"


def bool_to_word(b):
    return "Yes" if b else "No"


def count_sheep(sheep):
    return sum(1 for s in sheep if s is True)


def correct_tail(body, tail):
    return body[-1] == tail