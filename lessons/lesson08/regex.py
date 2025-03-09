import re


text = """Python For Beginners
Welcome! Are you completely new to 1986 programming? If not then we presume you will be looking for information about why and how to get started with Python. Fortunately an experienced programmer in any programming 25 language (whatever it may be) can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!
Python
"""
# pattern = "Pyt"
# result = re.match(pattern, text)
# print(result)
# result = re.search(pattern, text)
# print(result)
# result = re.findall(pattern, text)
# print(result)

# result = re.sub("Py", "DDD", text)
# print(result)


# pattern = "[a-mM-Z]"
# result = re.findall(pattern, text)
# print(result)
# pattern = "\d"
# result = re.findall(pattern, text)
# print(result)

# pattern = ".e.."
# result = re.findall(pattern, text)
# print(result)

pattern = "[a-z]+"
result = re.findall(pattern, text)
print(result)