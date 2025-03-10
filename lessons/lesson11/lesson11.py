
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# print(a/b)

# print("End of program")

# "asd"+1
# d = {}
# d["a"]



# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except:
#     print("An error occurred")

# print("End of program")



# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except (ZeroDivisionError, NameError, ValueError) as err:
#     print("Error Occurred and Handled", type(err), err)

# print("End of program")





# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except ZeroDivisionError as err:
#     print("ZeroDivision Error!", type(err), err)
# except NameError:
#     print("Name Error!")
# except ValueError as err:
#     print("Value Error!", type(err), err)
# except Exception as err:
#     print("An error occurred", type(err), err)

# print("End of program")



# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except ZeroDivisionError as err:
#     print("ZeroDivision Error!", type(err), err)
# except ArithmeticError as err:
#     print("Arithmetic Error!", type(err), err)




# print("End of program")



# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except ZeroDivisionError as err:
#     print("ZeroDivision Error!", type(err), err)
# except NameError:
#     print("Name Error!")
# except ValueError as err:
#     print("Value Error!", type(err), err)
# except Exception as err:
#     print("An error occurred", type(err), err)
# else:
#     print("No error occurred")
# finally:
#     print("This block will always execute")

# print("End of program")

# def f(a):
#     try:
#         return a*5
#     except:
#         return "An error occurred"
#     finally:
#         return "Finally block"


# print(f(5))


# try:
#     number = input("Enter a number: ")
#     if not number.isdigit():
#         raise ValueError("Invalid input")
# except ValueError as err:
#     print("An error occurred", type(err), err)

# number = input("Enter a number: ")
# if not number.isdigit():
#     # raise ValueError("Invalid input dsvbfkbnfdkgh kfg h")
#     # raise "dfhgv jfd" #TypeError: exceptions must derive from BaseException

class MyError(Exception):
    pass
    # def __init__(self, message):
    #     self.message = message
    # def __str__(self):
    #     return self.message


number = input("Enter a number: ")
if not number.isdigit():
    raise MyError("Invalid input dsvbfkbnfdkgh kfg h")
    