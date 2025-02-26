#zen
text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
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
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#підрахунки слів
better_count = text.lower().count("better")
never_count = text.lower().count("never")
is_count = text.lower().count("is")

print(f"Кількість слів 'better': {better_count}")
print(f"Кількість слів 'never': {never_count}")
print(f"Кількість слів 'is': {is_count}")

#текст в верхньому регістрі
upper_text = text.upper()

#заміна всіх i на & 
modified_text = upper_text.replace("I", "&")