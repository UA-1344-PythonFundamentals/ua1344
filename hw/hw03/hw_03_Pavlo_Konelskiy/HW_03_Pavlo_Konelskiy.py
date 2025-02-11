#first task

text_philosophy = "Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silentlyUnless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"

#print(text_philosophy)

count_better = text_philosophy.count("better")
count_never = text_philosophy.count("never")
count_is = text_philosophy.count("is")

print(f"The word count 'better': {count_better}, 'never': {count_never}, 'is': {count_is}")

text_upper = text_philosophy.upper()
print("The text in uppercase: \n" + text_upper)

replacing_letters = text_philosophy.replace("i", "&")

print("The text with replaced 'i' with '&': \n" + replacing_letters)


#second task

number = 3247

product = 1
for i in str(number):
    product *= int(i)
print(f"The product: {product}")

reversed_number = str(number)[::-1]
print(f"The reversed number: {reversed_number}")

sorted_numbers = ""

digits = list(str(number))

for i in range(len(digits)):
    for j in range(i + 1, len(digits)):
        if digits[i] > digits[j]:
            digits[i], digits[j] = digits[j], digits[i]

for digit in digits:
    sorted_numbers += digit

print(f"The sorted number: {sorted_numbers}")

#third task

a = 1
b = 4

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
