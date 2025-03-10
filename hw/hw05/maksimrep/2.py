n = int(input("Entered the number of elements n: "))

# start values
a_b = [0, 1]
summ = 0

for i in range(2, n):
    summ=a_b[i-2]+a_b[i-1]
    a_b.append(summ)
    
print("List:", a_b)