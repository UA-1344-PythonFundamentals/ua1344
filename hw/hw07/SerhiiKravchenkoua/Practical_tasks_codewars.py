#1.
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# The error is that the code after the return will not be executed.
# You have a return on the first line of the function,
# so the check if name == "Johnny": will never be reached.

#2.
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(char) == 1 else ')' for char in word)

#3.
def find_outlier(integers):
    first_three = integers[:3]

    even_count = sum(1 for num in first_three if num % 2 == 0)
    odd_count = sum(1 for num in first_three if num % 2 != 0)

    majority_even = even_count > odd_count

    for num in integers:
        if majority_even and num % 2 != 0:
            return(num)
        elif not majority_even and num % 2 ==0:
            return(num)

#4.
def filter_words(st):
    words = st.strip().split()

    formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]

    return ' '.join(formatted_words)

#5.
def number_to_string(num):
    return str(num)

#6.
def reverse(st):
    words = st.strip().split()
    return ' '.join(reversed(words))

#7.
def reverse_list(l):
    l.reverse()
    return l

#8.
def solution(number):
    if number < 0:
        return 0
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

#9.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    all_distance = fuel_left * mpg
    return all_distance >= distance_to_pump

#10.
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

#11.
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

#12.
def count_sheeps(sheep):
    count = 0
    for sheep_number in sheep:
        if sheep_number == True:
            count += 1
    return count

#13.
def correct_tail(body, tail):
    return body[-1] == tail