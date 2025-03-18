# doubled_odds = [n * 2 for n in range(10) if n % 2 == 1]

# print(doubled_odds)


# doubled_odds = []

# for n in range(20):
#     if n % 2 == 1:
#         doubled_odds.append(n * 2)

# print(doubled_odds)
# doubled_odds = {n * 2 for n in range(10) if n % 2 == 1}
# print(doubled_odds)
# doubled_odds = {n:n * 2 for n in range(10) if n % 2 == 1}
# print(doubled_odds)


# doubled_odds = (n * 2 for n in range(10) if n % 2 == 1)
# print(doubled_odds)
# print(next(doubled_odds))
# print(next(doubled_odds))
# for e in doubled_odds:
#     print(f"e:{e}")

# print(map(str, range(5)))

# n = 10
# l = [i*i for i in range(n)]
# t = (i*i for i in range(n))
# print(f"l:{l.__sizeof__()} {l}")
# print(f"t:{t.__sizeof__()} {t}")

# n = 100
# l = [i*i for i in range(n)]
# t = (i*i for i in range(n))
# print(f"l:{l.__sizeof__()} {l}"[:100])
# print(f"t:{t.__sizeof__()} {t}"[:100])

# n = 1000
# l = [i*i for i in range(n)]
# t = (i*i for i in range(n))
# print(f"l:{l.__sizeof__()} {l}"[:100])
# print(f"t:{t.__sizeof__()} {t}"[:100])



# l = [1,20,333]
# i = iter(l)
# print(i)
# print(next(i), i)
# print(next(i), i)
# print(next(i), i)
# print(next(i), i)



# list_number = ["raspberry", "grapes", "orange"]
# for value in list_number:
#     print(value)


# class MyList:
#     def __init__(self, iter):
#         self.data = iter
#         self.i = None
#     def __str__(self):
#         return f"{self.data}"
    
#     def __iter__(self):
#         print("__iter__")
#         if not self.i:
#             self.i = 0
#         return self
#     def __next__(self):
#         print("__next__")
#         try:
#             value = self.data[self.i]
#         except IndexError:
#             raise StopIteration()
#         self.i += 1
#         return value


# m = MyList(["raspberry", "grapes", "orange"])
# print("start for")
# for e in m:
#     print("step:")
#     print(e)

# print("end")



# class MyRange:
#     def __init__(self, start, end=None, step=1):
#         if end is None:
#             self.start = 0
#             self.end = start
#         else:
#             self.start = start
#             self.end = end
#         self.step = step

#     def __str__(self):
#         return f"MyRange({self.start}, {self.end}, {self.step})"
    
#     def __iter__(self):
#         print("__iter__")
#         self.i = self.start
#         return self
    
#     def __next__(self):
#         value = self.i
#         self.i += self.step
#         if value > self.end:
#             raise StopIteration("my")
#         return value


# r1 = MyRange(10)
# r2 = MyRange(-10,10)
# r3 = MyRange(-10, 10, 2)

# print(r1)
# print(r2)
# print(r3)

# print(list(r1))
# print(list(r2))
# print(list(r3))


# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     print("2")
#     yield 'b'
#     print("3")
#     yield 'c'

# print(my_generator)
# g = my_generator()
# print(g)
# print("===========")
# print(f"1:{next(g)}")
# print("===========")
# print(f"2:{next(g)}")
# print("===========")
# print(f"3:{next(g)}")
# print("===========")
# print(f"{next(g)}")


# import sqlite3



# def get_sql_user(_from, _to, count=10):
#     sql = "SELECT * FROM USERS LIMIT {} OFSET {};"
#     while _to > _from:
#         s = sql.format(count, _from)
#         yield s
#         return 10
#         _from += count
    

# sql_u = get_sql_user(100, 300, 50)
# sql_u2 = get_sql_user(10, 39, 3)
# sql_u3 = get_sql_user(152, 300, 82)
# for u in sql_u:
#     print(u)
# for u in sql_u2:
#     print(u)
# for u in sql_u3:
#     print(u)


from users_db import database_file

import sqlite3


def get_sql_user(_from, _to, count=10):
    sql = "SELECT * FROM USERS LIMIT {} OFFSET {};"

    while _to > _from:

        try:
            conn = sqlite3.connect(database_file)
            cursor = conn.cursor()

            cursor.execute(sql.format(count, _from))
            users = cursor.fetchall()

            yield users
            _from += count
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

        finally:
            if conn:
                conn.close()
for u in get_sql_user(3, 10, 2):
    print(u)
    import time
    time.sleep(2)