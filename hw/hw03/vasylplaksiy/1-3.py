# task 1
text = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!"""

# task 1 part 1
print("better count = ", text.lower().count("better"))
print("never count = ", text.lower().count("never"))
print("is count = ", text.lower().count("is"))

# task 1 part 2
print(text.upper())

# task 1 part 3
print(text.replace("i", "&"))




# task 2
print("\n\n\n#task 2\n")
number = 3254
# task 2 part 1
asList = list(map(str, str(number)))
listProduct = 1
for n in asList:
    listProduct = int(n) * listProduct
print("original number -", number)
print("product -", listProduct)
# task 2 part 2
asListReversed = asList.copy()
asListReversed.reverse()
print("reversed -", "".join(asListReversed))
# task 2 part 3
asListSorted = asList.copy()
asListSorted.sort()
print("sorted -", "".join(asListSorted))

# task 3
print("\n\n\n#task 3\n")
x = 12
y = 2
print(f"before interchange x={x}, y={y}")
x,y=y,x
print(f"after interchange x={x}, y={y}")