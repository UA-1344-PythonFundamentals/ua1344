print("#task1")
def getLargest(n1,n2):
    """return the largest number of two numbers"""
    if n1>=n2: return n1
    else: return n2
print(getLargest(float(input("write number 1:")),float(input("write number 2:"))))

print("#task2")
import math
areaCircle = lambda r: math.pi * r ** 2
areaRectangle = lambda w, l : w * l
areaTriangle = lambda b, h :  0.5 * (b * h)
print("areaCircle", areaCircle(float(input("circle radius:"))))
print("areaRectangle", areaRectangle(float(input("rectangle width:")), float(input("rectangle length:"))))
print("areaTriangle", areaTriangle(float(input("triangle base:")), float(input("triangle height:"))))

print("#task3")
def countChars(line):
    data = {}
    for s in line:
        if s in data: data[s] += 1
        else: data[s] = 1
    return data
print(countChars(input("write string:")))