#You need to write Python's philosophy in the string format:
#- find separately the number of occurrences of the words
#"better", "never" and "is" in the given line
#- you need to display all text in uppercase (all letters in uppercase)
#- replace all occurrences of the symbol "i" with "&"


zen = "Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren't special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you're Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it's a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let's do more of those!"

print('Zen:',zen)

#- find separately the number of occurrences of the words
#"better", "never" and "is" in the given line
print('Zen has word "better":',zen.count("better"), 'times')
print('Zen has word "never":',zen.count("never"), 'times')
print('Zen has word "is":',zen.count("is"), 'times')


#- you need to display all text in uppercase (all letters in uppercase)
print('Zen in uppercase:',zen.upper())

#- replace all occurrences of the symbol "i" with "&"
print('Replaced zen:',zen.replace('i','&'))