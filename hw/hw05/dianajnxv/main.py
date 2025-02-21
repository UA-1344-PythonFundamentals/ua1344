#task1
my_list = [1, 2, 3, 44, 35, 66, 70]
for i in my_list:
    print(float(i))
    
    
#task 2
num1 = 0
num2 = 1
n = 20

while num1 < 20:
    print(num1)
    num1, num2 = num2, num1 + num2

#task 3

n = int(input("Type a number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print(fact)


