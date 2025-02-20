# ## List
# l = list()
# print(type(l), l)
# l = list("test")
# print(type(l), l)
# # l = list(10) #TypeError: 'int' object is not iterable
# l = []
# print(type(l), l)
# l = [10, "test", 4]
# print(type(l), l)

# l = [1, 2, 3, 4, [5, 6, 7, 8]]
# print(l)
# print(l[1])
# print(l[4])
# print(l[4][1])
# # print(l[4][1][1])TypeError: 'int' object is not subscriptable
# print(l[-1])
# print(l[-1][-1])
# # print(l[10]) #IndexError: list index out of range
# ll = l[2:-2]
# print(ll)
# print(l[:-2])
# print(l[2:])
# print(l[2::2])

# l1 = [1,2,3] 
# l2 = ["a", (2,3)]
# l3 = l1 + l2 
# print(l1+l2)
# print(l3)
# # print(l1 + (1,2,3))#TypeError: can only concatenate list (not "tuple") to list
# print(l1 + list((1,2,3)))
# print(l1*5)

# l1[2] = 25
# print(l1)

# l = [
#     [1,2,3],
#     [4,[1,2,3],6],
#     [7,8,9, None],
#     10
# ]
# ll = l*2
# print(ll)
# l[0][1] = 999
# l[3] = "999"
# print(l)
# print(ll)
# ll[0][0] = "test"
# ll[3] = "YYY"

# print(ll)
# print()
# print(l)
# print(4 in l)
# print("999" in l)
# print("999" not in  l)
# x = ['test', 999, 3]
# print(['test', 999, 3]  in  l)
# print(x  is  l)
# print(id(x)  , id(l[0]))
# print(x == l[0])

# print("list:", [method for method in dir(list) if not method.startswith("_")])

# l = []
# l.append(1)
# print(l)
# l.append([1,2,3])
# print(l)
# l.clear()
# print(l)
# l = []
# print(l)
# row = [1,2,3]
# matrix = [row, row, row]
# print(matrix)
# matrix[0] = []
# print(matrix)
# row.clear()
# print(matrix)

# ll = l.copy()
# print(l, ll)
# l[0] = 99
# l[1][1] = "test"
# print(l, ll)

# import copy

# ll = l.copy()
# lll = copy.deepcopy(l)
# print(l, ll, lll)
# l[0] = 99
# l[1][1] = "test"
# print(l, ll, lll)
# from random import randint
# l = [randint(0, 3) for _ in range(10)]
# print(l)
# print(l.count(0))
# l = [1, 3, 3, 3, 1, 1, 0, 3, 0, 1]

# print(l)
# l.append(1)
# print(l)
# l.append("text")
# print(l)
# # l.extend(1)#TypeError: 'int' object is not iterable

# l.extend("text")
# print(l)
# print(l.index(0))
# x = l.pop()
# print(x, l)
# x = l.pop(5)
# print(x, l)
# x = l.remove("t")
# print(x, l)
# l.reverse()
# print(l)
# print("a"<"s")
# # 1<"s"TypeError: '<' not supported between instances of 'int' and 'str'
# # l.sort()#TypeError: '<' not supported between instances of 'int' and 'str
# ll = l[3:]
# print(l, ll)
# ll.sort()
# print(l, ll)
# l.sort(key=lambda element: id(element))
# print(l)

# is_true = ["asd", 1, [55]]
# is_false = ["", 0, []]
# is_some = ["", 1, [], "test"]
# print(f"{all(is_true)=}, {all(is_false)=}, {all(is_some)=}") 
# print(f"{any(is_true)=}, {any(is_false)=}, {any(is_some)=}") 

# print(list(enumerate(is_true)))
# print(len(is_true))
# # print(max(is_true))#TypeError: '>' not supported between instances of 'int' and 'str'
# l = [2,543,5,564,32,3,54,76,87]
# print(l)
# print(max(l), min(l))
# s = sorted(l)
# print(l)
# print(s)
# print(sum(l))


# tupl

# t = tuple()
# print(type(t), t)
# t = tuple("test")
# print(type(t), t)

# t = ()
# print(type(t), t)
# t = (1,2,[1,23])
# print(type(t), t)
# t = ("str") #<class 'str'> str
# print(type(t), t)
# t = ("str",) 
# print(type(t), t)

# print("tuple:", [method for method in dir(tuple) if not method.startswith("_")])

# l =(1,2,3,[1,2,3])
# print(l[1])
# print(l[-1])
# # l[1] = 5 #TypeError: 'tuple' object does not support item assignment
# l[-1].append("test")
# print(l)
# # l[-1] = [] #TypeError: 'tuple' object does not support item assignment



# ## set
# s = set()
# print(type(s), s)
# s = set("tests")
# print(type(s), s)
# s = {}#<class 'dict'> {}
# print(type(s), s)
# s = {1,2,3,1,2,3,4,2,1}
# print(type(s), s)
# # s[0]#TypeError: 'set' object is not subscriptable

# print("set:", [method for method in dir(set) if not method.startswith("_")])

# s = {1,2,3}
# s.add(4)
# print(s)
# s.add(3)
# # s.add([1,2,3]) #TypeError: unhashable type: 'list'
# print(s)
# print(s.pop())
# # print(s.pop(1))#TypeError: set.pop() takes no arguments (1 given)
# print(s)
# s.remove(2)
# # s.remove(22)#KeyError: 22
# print(s)
# s.add("tets")
# print(s)
# s.update("tets")
# print(s)


## dict

d = dict()
print(type(d), d)
# d = dict("jhdsbkjv")#ValueError: dictionary update sequence element #0 has length 1; 2 is required
data = [
    ("key", 10), 
    [1, 99],
    {3,2}
]
d = dict(data)
print(type(d), d)

d = {}
print(type(d), d)

d = {
    "key": "value1",
    10: "value2",
    (1,2,3): "value3",

}
print(type(d), d)
print(d[10])
print(d["key"])
print(d[(1,2,3)])
d[(1,2,3)] = 10
print(d)
# print(d[55])#KeyError: 55
d[55]=99
d["55"]="value2"
d[5]="value2"
print(d)

# print("set:", [method for method in dir(set) if not method.startswith("_")])
# from_delete = []
# print(d)
# for key in d:
#     if d[key] == "value2":
#         from_delete.append(key)
# for key in from_delete:
#     d.pop(key)
        
# print(d)

print("dict:", [method for method in dir(dict) if not method.startswith("_")])

# # print(d[33])#KeyError: 33
# print(d.get(33))
# print(d.get(33, "empty"))
# print(d.get(5))
# print(d.pop(55))
# print(d)
# print(d.popitem())
# print(d.update({"k1":1, "k3": 3}))
# print(d)
# dd = d.fromkeys("abcd", 1)
# print(dd)
print(d.items())
print(d.values())
print(d.keys())

for key in d:
    print(key, d[key])

for i in d:
    print(i, d[i])

a, b = 1,2
for key, value in d.items():
    print(key, value)
for i, j in d.items():
    print(i, j)


# d[[1]] = 1 #TypeError: unhashable type: 'list'
class A:pass
a = A()
d[a] = 15
print(d)

class B:
    __hash__ = None
b = B()
d[b] = "bb"
print(d)