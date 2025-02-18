# task 1

# zen
text ="""the zen of python, by tim peters
beautiful is better than ugly.
explicit is better than implicit.
simple is better than complex.
complex is better than complicated.
flat is better than nested.
sparse is better than dense.
readability counts.
special cases aren't special enough to break the rules.
although practicality beats purity.
errors should never pass silently.
unless explicitly silenced.
in the face of ambiguity, refuse the temptation to guess.
there should be one-- and preferably only one --obvious way to do it.
although that way may not be obvious at first unless you're dutch.
now is better than never.
although never is often better than *right* now.
if the implementation is hard to explain, it's a bad idea.
if the implementation is easy to explain, it may be a good idea.
namespaces are one honking great idea -- let's do more of those!"""

# find separately the number of occurrences of the words "better", "never", and "is"
better_count = text.lower().count("better")
never_count = text.lower().count("never")
is_count = text.lower().count("is")

# you need to display all text in uppercase (all letters in uppercase)

text_uppercase = text.upper()

# replace all occurrences of the symbol “i” with “&”
text_replaced = text.replace("i", "&").upper()

# results
print(f"occurrences of 'better': {better_count}")
print(f"occurrences of 'never': {never_count}")
print(f"occurrences of 'is': {is_count}")
print(f"text in uppercase: {text_uppercase}")
print(f"text with 'i' replaced: {text_replaced}")


# task 2

number = 6768

# convert the number to a string to manipulate its digits
str_num = str(number)

# find the product of the digits of this number

product = 1
for digit in str_num:
    product *= int(digit)

# write the number in reverse order

reversed_num = str_num[::-1]

# in ascending order, you need to sort the numbers included in the given number

sorted_digits = ''.join(sorted(str_num))

# results
print(f"product of digits: {product}")
print(f"reversed number: {reversed_num}")
print(f"digits in ascending order: {sorted_digits}")


# Task 3

a = 7
b = 17

# swap values without using a third variable
a, b = b, a

# results
print(f"a: {a}")
print(f"b: {b}")
