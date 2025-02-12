#task 1
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
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!"""

print(text.upper().replace("I", "&"))

print(text.count("better"))
print(text.count("never"))
print(text.count("is"))

#task 2
num = 3561
num1 = 3 * 5 * 6 * 1
print("The product of digits is: ", num1)

reversed_num = int(str(num)[::-1])
print("Reversed order is: ", reversed_num)

sorted_num = int("".join(sorted(str(num))))
print("The ascending order is: ", sorted_num)

#task 3
a = 31
b = 10

a, b = b, a  

print(a)  
print(b)  
