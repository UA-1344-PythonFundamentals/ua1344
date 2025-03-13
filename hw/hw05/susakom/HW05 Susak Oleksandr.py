# HW05 Susak Oleksandr
list_var=[1, 3, 5, 7, 23, 192, 389, 67, 356, 0, 936]
for type_of_var in list_var:
    type_of_var=float(type_of_var)
    print(type(type_of_var))

# Fibonacci numbers
fibon_num=int(input("Entered the number of elements="))
fibo_list=[0, 1]
fibo_sum=0
for i in range(2, fibon_num):
    fibo_sum=fibo_list[i-2]+fibo_list[i-1]
    fibo_list.append(fibo_sum)
print("Fibonacci list=", fibo_list)

factorial_number=int(input("Enter number for calculation="))
factorial_list=[]
for j in range(1,factorial_number+1):
    factorial_list.append(j)
multipy=1
for res in factorial_list:
    multipy=multipy*factorial_list[res-1]
print("Factorial=", multipy)