
# class User:
#     """A simple attempt to model a user."""
#     pass

# user_1 = User()

# print(type(user_1)) 


# class User:
#     """A simple attempt to model a user."""
#     def print(self):
#         print('Hello User')
#     def _print(self):
#         print('Hello User')
#     def __print(self):
#         print('Hello User')

# user_1 = User()

# user_1.print()
# print(type(user_1.print))
# print(type(user_1._print))
# print(type (user_1._User__print))

# class User:
#     count = 0
#     def print(self):
#         print(f'print - {self.count}')



# print(User.count)

# user_1 = User()

# user_1.print()
# User.count = 2
# user_1.print()
# user_2 = User()
# user_2.print()

# class User:
#     pass

# def print_user(obj):
#     print('Hello User -> ', type(obj), obj)


# print_user("test")
# print_user(35)
# # print_user()#TypeError: print_user() missing 1 required positional argument: 'obj'
# print(User.__dict__)

# User.p = print_user

# user_1 = User()
# user_1.p()
# print(User.__dict__)
# print(user_1.__dict__)
# # User.p()#TypeError: print_user() missing 1 required positional argument: 'obj'
# User.p(user_1)

# class DefClass: 
#     pass
# def_class_keys = list(DefClass.__dict__.keys())
# print("def_class_keys:",def_class_keys)
# class MyClass:

#     cm = ["Class"]
#     ci = 10
#     def __init__(self):
#         print('Hello from __init__', self.__dict__)

#         self.im = ["instance"]
#         print('__init__', self.__dict__)
#         self.ii = 20
#         print('end __init__', self.__dict__)
#     def print(self):
#         print(f"cm:{self.cm} ci:{self.ci} im:{self.im} ii:{self.ii}")

# print({key:value for key, value in MyClass.__dict__.items() if key not in def_class_keys})


# my_class1 = MyClass()
# print("my_class1: ", my_class1.__dict__)
# my_class2 = MyClass()
# print("my_class1: ", my_class2.__dict__)

# my_class1.print()
# my_class1.print()
# my_class1.im.append("new")
# my_class1.ii = 30
# my_class2.im.append("text")
# my_class2.ii = "test"
# print()
# my_class1.print()
# my_class2.print()
# MyClass.cm.append("new Class") 
# MyClass.ci = 30
# print()
# my_class1.print()
# my_class2.print()

# my_class1.cm.append("instance")
# my_class2.ci = 40
# print()
# my_class1.print()
# my_class2.print()
# print(MyClass.ci)

# print()
# print({key:value for key, value in MyClass.__dict__.items() if key not in def_class_keys})
# print("my_class1: ", my_class1.__dict__)
# print("my_class1: ", my_class2.__dict__)

# m = MyClass()
# m.print()
