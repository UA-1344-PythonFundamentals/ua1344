philosophy = """1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one-- and preferably only one --obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than *right* now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!
20. Beautiful is better than ugly.
21. Explicit is better than implicit.
22. Simple is better than complex.
23. Complex is better than complicated.
24. Flat is better than nested.
25. Sparse is better than dense.
26. Readability counts."""
print(type(philosophy))

print("Number of occurrence of better:", philosophy.count("better"))
print("Number of occurrence of never:", philosophy.count("never"))
print("Number of occurrence of is:", philosophy.count("is"))

print(philosophy.upper())

print(philosophy.replace("i", "&"))


num = 3548
product_of_digit = 1
for digit in str(num):
    product_of_digit *=int(digit)
print(product_of_digit)

reversed_num = int(str(num)[::-1])
print(reversed_num)

digits = list(str(num))
digits.sort()
sorted_digits_ascending = int("".join(digits))
print(sorted_digits_ascending)


happiness = 1
unhappiness = 100
happiness, unhappiness = unhappiness, happiness
print(happiness)
print(unhappiness)