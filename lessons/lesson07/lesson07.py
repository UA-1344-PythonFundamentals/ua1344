# def my_func():
#     """ this function is cool
#         return: None
#     """
#     print("start fukc")
#     print("\tfukc")
#     print("end fukc")

# print("run")


# my_func()
# my_func()
# my_func()
# print(my_func)
# f = my_func
# f()

# print(print.__doc__)
# help(print)
# print(my_func.__doc__)
# help(my_func)

# def multy_print(text, count):
#     while True:
#         print(text)
#         if count <=0:
#             return
#         print("end while")
#         count -= 1

# # multy_print("test", 3)
# # multy_print("2", 5)

# def my_sum(a, b):
#     c = a+b
#     return c

# print(my_sum(52, 98))
# x = my_sum(-18, 99)
# print(x)

# def f(number):
#     if type(number) in (int, float):
#         return number**number
#     elif type(number) is list:
#         return
    


# print(f(9))
# print(f("9"))
# print(f([]))


# def print_info(name, age):
#     print("="*10)
#     print(f"\t name: {name}")
#     print(f"\t age: {age}")
#     print("="*10)

# print_info() #TypeError: print_info() missing 2 required positional arguments: 'name' and 'age'
# print_info("Liubomyr") #TypeError: print_info() missing 1 required positional argument: 'age'
# print_info("Liubomyr", 38) 
# print_info("Liubomyr", 38, "Lviv") #TypeError: print_info() takes 2 positional arguments but 3 were given

# def print_info(name, age, city="Lviv"):
#     print("="*10)
#     print(f"\t name: {name}")
#     print(f"\t age: {age}")
#     print(f"\t city: {city}")
#     print("="*10)

# # print_info("Liubomyr")  #TypeError: print_info() missing 1 required positional argument: 'age'
# print_info("Liubomyr", 38) 
# print_info("Liubomyr", 38, "Odesa") 
# # print_info("Liubomyr", 38, "Odesa", "UK") #TypeError: print_info() takes from 2 to 3 positional arguments but 4 were given
# print_info(38, "Odesa", "Liubomyr") 


# print_info(age=38, city="Odesa", name="Liubomyr") 


# def print_info(name, age=18, city="Lviv"):
#     print("="*10)
#     print(f"\t name: {name}")
#     print(f"\t age: {age}")
#     print(f"\t city: {city}")
#     print("="*10)



# print_info("Vasyl", city="Franyk") 


# def print_names(*names):
#     print("="*10)
#     print(f"{names}")
#     for name in names:
#         print("\t", name)
#     print("="*10)

# print_names("oleh", "Liubomyr", "taras")
# print_names(15, "oleh", "Liubomyr", 29, "taras")
# # print_names(15, "oleh", "Liubomyr", 29, "taras", k= 55) #TypeError: print_names() got an unexpected keyword argument 'k'

# def f(*args, **kwarg):
#     print(f"{args=} {kwarg=}")

# f()
# f(1,2,3,4, a=1, b=2, c=3)


# def f(a, b=1, c):#SyntaxError: parameter without a default follows parameter with a default
#     pass

# print("a", sep="=", 15)# SyntaxError: positional argument follows keyword argument
# def f(a, b, *args, d=4, e=5, **kwarg):
#     print(f"{a=} {b=} {args=} {d=} {e=} {kwarg=}")

# f(10, 20, 30, 40, 50, 60, d=44, f=100, g=999)


# a = 101333
# b = [1,2,3]
# print(f"{id(a)=}, {id(b)=}")
# def g(x, y):
#     print(f"{id(x)=}, {id(y)=}")
#     x += 1
#     y.append(4)
#     print(f"{id(x)=}, {id(y)=}")
#     print(x, y)
# g(a, b)
# print(a, b)


# x = 10
# def f(n):
#     k = n*n
#     n += 10
#     print(dir())
#     print(f"{k=} {n=}")

# f(x)

# print(dir())
# print(f"{x=}")
# # print(k)#NameError: name 'k' is not defined


# x = "global"

# def f():
#     print("=> func start")
#     # x = "local"
#     print("\t", x)
#     print("=> func end")

# f()
# print(x)



# x = "global"

# def f():
#     print("=> func start")
#     print("\t", x) #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#     x = "local"
#     print("\t", x)
#     print("=> func end")

# f()
# print(x)




# x = "global"

# def f():
#     global x
#     print("=> func start")
#     print("\t", x) 
#     x = "local"
#     print("\t", x)
#     print("=> func end")

# f()
# print(x)


# x = "global"

# def l1():
#     l_1 = "local l1"
#     def l2():
#         nonlocal l_1
#         l_2 = "local l2"
#         l_1 = "l_1, local l2"
#         print("l2() -> ", locals())
#     l2()
#     print("l1() -> ", locals())

# l1()
# print("global: ", dir())

# def f():
#     f1()
#     f2()
# # import random
# # f()

# def f1():
#     print("f1")


# def f2():
#     print("f2")


# f()


# def f():
#     print("f1")
# f()

# def f():
#     print("f2")
# f()

# print(sum([1,2,3,54,6,78]))
# s = sum
# def sum(a, b):
#     return a+b


# # print(sum([1,2,3,54,6,78])) #TypeError: sum() missing 1 required positional argument: 'b'
# print(sum(2,6))
# sum = s

# print(sum([1,2,3,54,6,78]))



# def rec(in_param):
#     # print(in_param)
#     rec(in_param)

# import sys
# # sys.setrecursionlimit(3000)

# rec(1)


# def rec(in_param, level=0):
    
#     if in_param<5:
#         print("*"*level, in_param)
#         rec(in_param + 1, level=level+1)
#         print("*"*level, in_param)
#     else:
#         print(f"{" "*level}rec({in_param})")
    
# rec(1)


# # 5!
# n = int(input("set n!: "))
# f = 1
# for i in range(1, n+1):
#     f *= i
# print(f"{n}! = {f}")

# def fuct(n):
#     if n <=0:
#         return 1
#     else:
#         return n*fuct(n-1)
# print(f"{n}! = {fuct(n)}")



# def f(a, b):
#     return a+b
# g = lambda a, b: a+b

# f(1,2)
# f(1,2)



l = [1,2,8,"test", 9.8, 3, 5, "16"]

l.sort(key=lambda e: len(e) if type(e) is str else e)
print(l)

def my_s(element):
    if type(element) is str:
        return -len(element)
    else:
        return -element

l.sort(key=my_s)
print(l)