#Task1. In the range from 1 to 10 determine
#• even numbers that are divisible by 2,
#• odd numbers, which are divisible by 3,
#• numbers that are not divisible by 2 and 3.
even_numbers = list()
odd_numbers = list()
other_numbers = list()

for i in range(1,11):
    if i%2 == 0 and i%3 != 0:
        even_numbers.append(i)
    elif i%3 == 0 and i%2 != 0:
        odd_numbers.append(i)
    elif i%3 == 0 and i%2 == 0:
        odd_numbers.append(i)
        even_numbers.append(i)
    else :
        other_numbers.append(i)
print(even_numbers)
print(odd_numbers)
print(other_numbers)
