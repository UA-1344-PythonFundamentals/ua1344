zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# 1.1 Find the number of occurrences of the words "better", "never" and "is".
print('Number of occurrences of the word "better":', zen.count('better'))
print('Number of occurrences of the word "never":', zen.count('never'))
print('Number of occurrences of the word "is":', zen.count('is'))
print("\n")

# 1.2 Display all text in uppercase.
print(zen.upper())

# 1.3 Replace all occurrences of the word "i" with "&".
print(zen.replace('i', '&'))

num = 9361
num_str = str(num)

# 2.1 Find product of digits of the number.
product = 1
for d in num_str:
    product *= int(d)
print(f'Product of digits of the number {num} is {product}\n')

# 2.2 Write the number in reverse order.
reversed_str = ''.join(num_str[::-1])
print(f'Reverse order of the number {num} is {reversed_str}\n')

# 2.3 Sort the digits of the number in ascending order.
sorted_str = ''.join(sorted(num_str))
print(f'Sorted digits of the number {num} in ascending order is {sorted_str}\n')

# 3 Interchange the values of two variables without using the third variable.
a = 10
b = 20
print(f'Before interchanging values of a and b: a = {a}, b = {b}')
a, b = b, a
print(f'After interchanging values of a and b: a = {a}, b = {b}')