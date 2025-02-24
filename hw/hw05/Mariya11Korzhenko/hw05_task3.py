#factorial

max = int(input("Enter number:"))
result = 1
n = 0
while n < max:
    result = result * (n + 1)
    n+=1
    
print (result)