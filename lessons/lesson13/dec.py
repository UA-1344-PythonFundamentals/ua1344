# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         result = func(*args, **kwargs)
#         print("*" * 30)
#         return result
#     return inner

# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner


# @star
# def add(a, b):
#     return f"{a}+{b}={a+b}"

# @percent
# @star
# def div(a, b):
#     print(f"{a}/{b}={a/b}")

# print(add(1,2))
# print(div(1,2))
# def dec(c="*", count=10):
#     def char(func):
#         def inner(*args, **kwargs):
#             print(c * count)
#             func(*args, **kwargs)
#             print(c * count)
#         return inner
#     return char

# @dec("+", 10)
# @dec("=", 20)
# @dec(">", 15)
# @dec("<", 25)
# def div(a, b):
#     print(f"{a}/{b}={a/b}")


# print(div(1,2))
# print(div(1,2))
# print(div(1,2))
# print(div(1,2))


def prin_log(fun):
    def inner(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = fun(*args, **kwargs)
        end = time.perf_counter()
        print(f"run funcrion {fun.__name__} {args=} {kwargs=} time:{end-start}")
        return result
    return inner



def cesh(fun):
    c={}
    def inner(*args, **kwargs):
        if c.get(args):
            result = c.get(args)
        else:
            result = fun(*args, **kwargs)
            c[args] = result
        return result
    return inner


@prin_log
@cesh
def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using recursion.

    Args:
        n (int): The index of the Fibonacci number to calculate (non-negative).

    Returns:
        int: The nth Fibonacci number.
        Returns None if n is negative.
    """
    if n < 0:
        return None  # Handle negative input
    elif n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

fibonacci_recursive(10)
