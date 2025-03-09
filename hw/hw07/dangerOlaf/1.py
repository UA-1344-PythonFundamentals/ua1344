#Write a function that returns the largest number of two numbers 
#(use DocStrings documentation strings in the function).

def compare(a,d):
    """The function compares two numbers, defines the biggest one and returns it"""
    return a if a >= d else d

print(compare(6,5))