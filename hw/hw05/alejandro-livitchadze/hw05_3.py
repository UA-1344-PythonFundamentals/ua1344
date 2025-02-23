def factorial(num):
    if num == 0:
        print(1)
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        print(result)

factorial(3)