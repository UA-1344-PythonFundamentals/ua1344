# class A:
#     def __init__(self):
#         self.x = 1
#         self._x = 10
#         self.__x = 100

#     def __str__(self):
#         return f"{self.x} {self._x} {self.__x}"
#     def __private(self):
#         print("This is private method")
    
# a = A()
# print(a)
# print(a.x)
# print(a._x)
# # print(a.__x)#AttributeError: 'A' object has no attribute '__x'
# print(a._A__x)
# # a.__private()#AttributeError: 'A' object has no attribute '__private'
# a._A__private()

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

    def __repr__(self):
        return f"({self.__x}, {self.__y})"
    
    def get_x(self):
        print("get_x")
        return self.__x
    def set_x(self, x):
        print("set_x")
        self.__x = x
    
    x = property(get_x, set_x, doc="This is x property")

    @property
    def y(self):
        print("get_y")
        return self.__y
    
    @y.setter
    def y(self, y):
        print("set_y")
        self.__y = y

    

point = Point(1, 2)
# print(point)
# print(point.get_x())
# point.set_x(10)
# print(point)
print(point.x)
point.x = 100

print(point.y)
point.y = 200
print(point)