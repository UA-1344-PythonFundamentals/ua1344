# obj = True
# print(type(obj), obj)
# obj = False
# print(type(obj), obj)
# obj = 12
# print(type(obj), obj)
# obj = 12.5
# print(type(obj), obj)
# obj = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# print(type(obj), obj)
# obj = ( 'abcd', 786 , 2.23, 'john', 70.2 )
# print(type(obj), obj)
# obj = "My name is ..."
# print(type(obj), obj)
# obj = set("My name is ...")
# print(type(obj), obj)
# obj = {
#     'name': 'john',
#     'id':6734,
#     'role': 'admin'
# }
# print(type(obj), obj)


# a = 21
# print(id(a), type(a), a)

# a = a +  10
# print(id(a), type(a), a)

# l = [1, 2, 3]
# print(id(l), type(l), l)
# l.append(4)
# print(id(l), type(l), l)

# print(type(1) is int)
# print(type(1) is float)
# print(type(1) == int)
# print(type(1) == float)

# print(10)
# print(15)
# a = 1 + 2 + 3 + 4 
# + 5 + 6 + 7 + 8 + 9 + 10
# print(a)
# a = 1 + 2 + 3 + 4 \
#     + 5 + 6 + 7 \
#     + 8 + 9 + 10
# print(a)
# print(20)
# print(25)
# print(30)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(l)
# l = [1, 2, 3, 
#      4, 5, 6, 7,
#        8, 9, 10]

# print(l)

# l = ["1, 2, 3, ",
#      "4, 5, 6, 7,"
#        "8, 9, 10"]

# print(l)


# for i in range(3):
#     print(">"*10)
#     print("\t", i)
#     print("\t", i**i)
#     print("<"*10)

# print("Done")


# a = 1
# b = 2
# c = 3
# print(a, b, c)
# a, b, c = 10, 20, 30
# print(a, b, c)

# a, b = b, a
# print(a, b)

# a =b =c = 99
# print(a, b, c)

# a = 1
# b = 2
# c = a
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)
# a = 99
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)


# a = [1]
# b = [2, a]
# c = a
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)
# a.append(99)
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)

# MY_NAME = "John"
# print(MY_NAME)
# MY_NAME = "Doe"
# print(MY_NAME)


# a= 10
# print(a)
# a= 0b10
# print(a)
# a= 0o10
# print(a)
# a= 0x10
# print(a)

# for i in range(30):
#     print(f"{bin(i)[2:]}\t{oct(i)[2:]}\t{i}\t{hex(i)[2:]}")

# a = 100_000_000_000_500
# print(type(a), a)
# a = 5.0
# print(type(a), a)
# a = .9
# print(type(a), a)
# a = 3.
# print(type(a), a)
# a = 3.14e5
# print(type(a), a)
# a = 314e-2
# print(type(a), a)

# a = (-1)**0.5
# print(type(a), a)


# obj = True
# print(type(obj), obj)
# obj = False
# print(type(obj), obj)

# # obj = None
# a = []  #list
# print(type(a), a)
# a = ()  #tupl
# print(type(a), a)
# a = {1,2,3,2,3,4,2,3,4}  #set
# print(type(a), a)
# a = {1:2,
#      2:2,
#      3:4,
#      4:3}  #set
# print(type(a), a)

# list, tuple, str
# a = "test"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])#IndexError: string index out of range
# s = set(a)
# print(s) 
# # print(s[1]) 

# d = {1:2, "test":3, 3:4}

# print(d[1])
# print(d["test"])

# a = 999**999
# print(a)
# print(len(str(a)))
# a = 99999**999
# # print(a)
# # print(len(str(a)))
# import sys
# sys.set_int_max_str_digits(9999)
# print(a)
# print(len(str(a)))

# text = "99"
# i = int(text)
# print(type(i), i)

# text = "1011010101"
# i = int(text, 2)
# print(type(i), i)

# text = "z"
# i = int(text, 36)
# print(type(i), i)
# text = "10"
# i = int(text, 36)
# print(type(i), i)

# l = [1, 2, 3, 4, 5]
# s = str(l)
# print(type(s), s)
# print(s[0])

# text = "Hello World"
# print(list(text))
# print(tuple(text))
# print(set(text))


# text = "Hello World"
# for c in text:
#     print(ord(c), c)

# for c in range(0, 255):
#     print(c , "\t", chr(c))

# text1 = "Hello"
# text2 = 'Hello'
# print(text1[1])
# text1[1] = "a"# TypeError: 'str' object does not support item assignment


# sql = """
# SELECT * FROM table 
# WHERE id = 1
# """

# print(sql)

# sql = "SELECT * FROM \ntable WHERE id = 1"

# print(sql)

# sql = "0123456789\rabcd"

# print(sql)

# sql = "0123456789\"rabcd"

# print(sql)

# template = "My name is %s and I am %d years old and I am %.3f tall"

# name = "John"
# age = 21
# height = 1.75
# print(template % (name, age, height))
# name = "Doe"
# age = 25
# height = 1.8555
# print(template % (name, age, height))

# template = "My name is {name} and I am {age} years old and I am {height} tall"
# name1 = "Doe"
# age2 = 25
# height3 = 1.8555

# print(template.format(height=height3, name=name1, age=age2))

# print(f"My name is {name1.upper()} and I am {age2**99} years old and I am {height3 +22 } tall")

text = "Hello. World."
# print(text[0])
# print(text[6])
# print(text[-1])
# print(text[-2])
# print(text[0:5])
# print(text[2:-2])
# print(text[:-2])
# print(text[3:])
# print(text[1:7:2])
# print(text[::2])

# print(text.upper())
# print(text.lower())
# text = "Hello World. Hello World."
# print(text.capitalize())
# print(">", text.center(50), "<", sep="")
# print(text.count("o"))
# print(text.count("Wo"))
# print(text.isdigit())
# text = "123456"
# print(text.isdigit())
# text = "HelloWorldHelloWorld"
# print(text.isalpha())

# a++
# a--
# ++a
# --a