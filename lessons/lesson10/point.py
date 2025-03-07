from random import randint


class Point:
    def __init__(self, x=0, y=0):
        print(f"Point {x} {y}")
        self.x = x
        self.y = y
        print(f"Point {self.__dict__} is created")

    # def __del__(self):
    #     print(f"Point({self.x}, {self.y}) is deleted")

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __lt__(self, other):
        return self.distance_to_the_origin() < other.distance_to_the_origin()
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def distance_to_the_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

    def distance(s, other):
        return ((s.x - other.x) ** 2 + (s.y - other.y) ** 2) ** 0.5


# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1.x, p1.y)
# print(p2.x, p2.y)

# print(p1.distance_to_the_origin())
# print(p2.distance_to_the_origin())
# print(p1, p2)
# pp = [p1, p2]
# print(pp)

# print(p1.distance(p2))
# del p1
# def print_points(count):
#     for i in range(count):
#         print(Point(i, i))

# print("*"*50)
# print_points(5)
# print("*"*50)

# def generate_points(count):
#     return [Point(randint(-10, 10), randint(-10, 10)) for _ in range(count)]

# points = generate_points(5)
# print(points)
# points.sort(key=lambda p: -p.distance_to_the_origin())
# print(points)
# points.sort()
# print(points)

# p = points[0] + points[1]
# print(p)

class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        print(f"Point3D {x} {y} {z}")
        super().__init__(x, y)
        self.z = z
        print(f"Point3D {self.__dict__} is created")

    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"
    
    def distance(s, other):
        return ((s.x - other.x) ** 2 + (s.y - other.y) ** 2 + (s.z - other.z)) ** 0.5
    
    def old_distance(s, other):
        return super().distance(other)
    # def distance(s, other, third):
    #     return ((s.x - other.x) ** 2 + (s.y - other.y) ** 2 + (s.z - other.z)) ** 0.5

p3d = Point3D(1, 2, 3)
print(p3d)
print(p3d.distance_to_the_origin())
# print(p3d.distance(Point3D(10, 10, 10)))
# p3d.dd()#AttributeError: 'Point3D' object has no attribute 'dd'

print(Point3D.__dict__)