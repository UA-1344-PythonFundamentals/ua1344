#Fibonacci sequence

max = int(input("Enter number:"))
result = [0]
while result[-1] < max:
    if(result[-1] == 0):
        result.append(1)
    else:
        if( result[-2]+result[-1] < max ):
            result.append(result[-2]+result[-1])
        else:
            break
    
print (result)
