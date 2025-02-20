# print("a")
# print("b")

# a = 1
# b = 2

# print(f"a==b is", a==b)
# print(f"a!=b is", a!=b)
# print(f"a<b is", a<b)
# print(f"a>b is", a>b)

# print(f"a < b and type(a) is int", a < b and type(a) is int)
# a = 1.0
# print(f"a < b and type(a) is int", a < b and type(a) is int)

# print(not True)
# print(not False)


# a = True
# b = False
# c = True

# print(a and b)
# print(b or c)
# print(b or c and a)
# print(c or b and a)
# print(False or b and a)

# print((c or b) and a)

# a = [1,2,3]
# b = [1,2,3]
# print(a == b) 
# print(a is b) 
# print(id(a) == id(b))
# print(a is not b)
# c = a
# print(a == c) 
# print(a is c) 
# print(id(a) == id(c))
# print(a is not c)

# text = "Hello World"
# print("Hello" in text)
# print("Hello" not in text)
# print("foo" not in text)
# # print(1 in text)#TypeError: 'in <string>' requires string as left operand, not int

# l = [1,2,3, "Hello", (9,8,7)]
# print(1 in l) 
# print("Hello" in l) 
# print(9 in l) 
# print((9,8,7) in l) 

# text1 = "Hello World"
# text2 = "Hello World"
# print(text1 == text2)
# print(id(text1), id(text2))
# print(text1 is text2)

# for i in range(200, 300):
#     ii = i
#     jj = i+1-1
#     print(ii, jj, ii == jj, ii is jj, id(ii), id(jj))


# status_code = int(input("Enter status code: "))

# if status_code >=100 and status_code < 200:
#     print("status code is")
#     print("\tInformational")
#     print("\tRequest received, continuing process")

# print("end of program")

# status_code = int(input("Enter status code: "))

# if status_code >=100 and status_code < 200:
#     print("status code is")
#     print("\tInformational")
#     print("\tRequest received, continuing process")
# else:
#     print("status code is not Informational")
#     print("\tRequest received, continuing process")

# print("end of program")

# age  = int(input("Enter your age: "))


# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')


# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')


# weather = "raining"
# print("Open Your umbrella" if weather == "raining" else "Wear your cap") # weather == "raining" ? "Open Your umbrella" : "Wear your cap"
# if weather == "raining":
#     print("Open Your umbrella")
# else:
#     print("Wear your cap")

# weather = "sunny"
# if weather == "raining": print("Open Your umbrella")
# else: print("Wear your cap")
# print("end of program")




# status_code = int(input("Enter status code: "))

# if status_code >=100 and status_code < 200:
#     print("status code is")
#     print("\tInformational")
#     print("\tRequest received, continuing process")
# elif status_code >=200 and status_code < 300:
#     print("status code is")
#     print("\tSuccess")
#     print("\tThe action was successfully received, understood, and accepted")
# elif status_code >=300 and status_code < 400:
#     print("status code is")
#     print("\tRedirection")
#     print("\tFurther action must be taken in order to complete the request")
# elif status_code >=400 and status_code < 500:
#     if status_code == 404:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe requested resource could not be found but may be available in the future")
#     elif status_code == 403:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe request was valid, but the server is refusing action")
#     elif status_code == 400:
#             print("status code is", status_code)
#             print("\tClient Error")
#             print("\tThe request contains bad syntax or cannot be fulfilled")
#     elif status_code == 401:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe request requires user authentication")
#     print("status code is")
#     print("\tClient Error")
#     print("\tThe request contains bad syntax or cannot be fulfilled")
# elif status_code >=500 and status_code < 600:
#     print("status code is")
#     print("\tServer Error")
#     print("\tThe server failed to fulfill an apparently valid request")


# status_code = int(input("Enter status code: "))

# match status_code:
#     case 400:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe request contains bad syntax or cannot be fulfilled")
#     case 401:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe request requires user authentication")
#     case 404:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe requested resource could not be found but may be available in the future")
#     case 403:
#         print("status code is", status_code)
#         print("\tClient Error")
#         print("\tThe request was valid, but the server is refusing action")
#     case _:
#         print("status code is", status_code)

# match status_code:
#     case 400:
#         print("Bad request")
#     case 401 | 403 as error:
#         print(f'{error} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")


# if status_code == 400:
#     print("Bad request")
# if status_code == 401 or status_code == 403:
#     print(f'{status_code} is authentication error')
# if status_code == 404:
#     print("Not found")
# else:
#     print("Other error")


# l = [
#     ("load", "http://www.google.com"),
#     ("save", "http://www.google.com", "file.txt"),
#     ("save", "http://www.google.com", "file.txt", "file2.txt", "file3.txt"),
#     ("save", "http://www.insta.com", "file_insta.txt", "file_insta2.txt", "file_insta3.txt", "file_insta4.txt", 15),
#     1,
#     ("click", "http://www.google.com"),
# ]
# for row in l:
#     print("parse row", row)
#     match row:
#         case ("load", url):
#             print("load", url)
#         case ("save", url, files):
#             print("save", url, files)
#         case ("save", url, *files):
#             print("save", url)
#             for file in files:
#                 print("\t", file)
#         case _:
#             print("Invalid row")
#     print(">>----------<<")

# value = True

# if value:
#     print(value ,"is True")
# else:
#     print(value ,"is False")


# value = False

# if value:
#     print(value ,"is True")
# else:
#     print(value ,"is False")

# value = []

# if value:
#     print(value ,"is True")
# else:
#     print(value ,"is False")

# is_false = [False, 0, 0.0, "", [], {}, (), None]
# is_true = [True, 199, 0.000001, " ", [1], {1:1}, (1,), "True"]

# for value in is_false + is_true:
#     if value:
#         print(value ,"is True")
#     else:
#         print(value ,"is False")


# if len(is_true)> 0: # incorrect
#     print("is_true is True")

# if is_true: #correct
#     print("is_true is True")

# print(True and [1,2,3] and "Hello") 
# print(True and [] and "Hello") 
# print(False or [1] or 0) 
# print(False or [] or 0) 

# l =[1,2,3]

# result = None
# if len(l)>0 and l[2]:
#     result = l[2]
   
# print(result)

# result = l and l[2]
# print(result)

# if 1:
#     result = "True"

# print(result)



is_false = [False, 0, 0.0, "", [], {}, (), None]
is_true = [True, 199, 0.000001, " ", [1], {1:1}, (1,), "True"]

value = False
if False:
    print(value ,"is True")
else:
    print(value ,"is False")

value = 0
if value:
    print(value ,"is True")
else:
    print(value ,"is False")


value = 0.0
if value:
    print(value ,"is True")
else:
    print(value ,"is False")