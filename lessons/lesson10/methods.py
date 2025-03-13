# class MyClass:

#     def my_method(self):
#         print('This is my method')
#         print(dir())
#         print(type(self), id(self))

#     @classmethod
#     def my_class_method(cls):
#         print('This is my class method')
#         print(dir())
#         print(type(cls), id(cls))

#     @staticmethod
#     def my_static_method():
#         print('This is my static method')
#         print(dir())
#         # print(type(self), id(self)) #NameError: name 'self' is not defined

# print(f"{id(MyClass)=}")
# m = MyClass()
# print(f"{id(m)=}")

# m.my_method()
# # MyClass.my_method() #TypeError: my_method() missing 1 required positional argument: 'self'

# m.my_class_method()
# MyClass.my_class_method()

# m.my_static_method()
# MyClass.my_static_method()