#Write a script that will calculate the factorial of the entered number without using recursion.
n = int(input('Please enter a number for factorial: '))
if n == 0:
    print("0! = 1")
elif n == 1:
    print("1! = 1")
elif n > 1:    
    result = str(n)+"! = 1"
    fac = 1
    for i in range(2,int(n+1)):
        result += "*"+str(i)
        fac *= i
    print(result,"=",str(fac))