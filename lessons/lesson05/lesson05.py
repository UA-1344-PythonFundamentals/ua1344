# def count_digits(number):
#     if type(number) not in [int]:
#         print("Wrong data type")
#     else:
#         if number < 0:
#             number = -number
#         num_str = str(number)
#         print(len(num_str))
#         # result = len(str(abs(number)))
#         # print(result)


# start = 0
# finish = 10

# while start < finish:
#     print(start)
#     start += 1
# # else:
# #     print ('The end')

# print("end program")


# start = 0
# finish = 10


# while start < finish:
#     print(start, finish)
#     finish +=1
#     start +=1

# print("end program")

# from time import sleep
# step = 1
# while True:
#     print(f"{step=}")
#     step +=1
#     sleep(1)


# for element in "text":
#     print(element)

# for element in ["text", None, [1,2,3], 5]:
#     print(f"element is >{element}<")
# # for element in 10: #TypeError: 'int' object is not iterable
#     print(f"element is >{element}<")
# l = range(10)
# print(l, list(l))

# for i in range(5):
#     print(i)

text = "some text"

# for i in text:
#     if i == 'e':
#         print(i)

# for i in range(len(text)):
#     if text[i] == 'e':
#         print(i, text[i])

# print(list(range(5)))
# print(list(range(5, 10)))
# print(list(range(5, 10, 2)))


# index_text = enumerate(text)
# print(list(index_text))

# for pair in enumerate(text):
#     print(f"{pair=}")
#     if pair[1] == 'e':
#         print(pair[0], pair[1])

# a, b = 1, 2
# print(a, b)

# print(list(enumerate(text)))
# for i, char in enumerate(text):
#     print(f"{i=} {char=}")
#     if char == 'e':
#         print(f"{i=} {char=}")

# d = {
#     "key1": "value1",
#     "key2": 2,
#     "key3": None
# }

# for key in d:
#     print(key, d[key])


text = "ndco87dsychds8v79dyhv87dsv7s8dg8"
s = 0
# for i in text:
#     print(i, i.isdigit())
#     if not i.isdigit():
#         continue
#     print(f"sum={s}+{i}=", end="")
#     s += int(i)
#     print(s)
# else:
#     print(f"{s=}")



# for i in text:
#     print(i, i.isdigit())
#     if not i.isdigit():
#         continue
#     if s > 20:
#         break
#     print(f"sum={s}+{i}=", end="")
#     s += int(i)
#     print(s)
# else:
#     print(f"{s=}")
# print(f"out for {s=}")

# while True:
#     x = input("enter x:")
#     if x.isdigit():
#         x = int(x)
#         break
#     else:
#         print("x is not a number")
# print(x*x)

# l = [0,1,2,3,4,5,6]
# for i in l:
#     print(i)
#     if i < len(l)-1:
#         l[i+1] += 1


# l = list(range(10))
# print(l)
# for i in l:
#     print(i)
#     if i%2:
#         print(l)
#         # del l[i]
#         del i

# print(l)

# a = "12345"
# for i in a:
#     print(i)
#     a += "+"
#     print(a)

# for i in range(10):
#     pass


# i = 0 
# while i < 100:
#     print(i, end=" ")
#     i += 2
# print()
# for i in range(0, 100, 2):
#     print(i, end=" ")

# i = 1
# while i < 100: 
#     print(i, end=" ") 
#     i += 2


# for i in range(100): 
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

# print()
# for i in range (1,100,2):
#     print(i, end=" ")
# print()


# for i in range (1,100,2):
#     print(i, end=" ")
# for i in range(0, 100):
#     print(i, end=" ")
#     if i % 2 != 0:
#         break


numbers = [2, 5, 8, 11]
for num in numbers:
    if num % 2:
        print("Yes:", num)
        break
else:
    print("No")


for i in range(0, 100):
    print(i, end=" ")
    if i % 2 == 0:
        break # another one