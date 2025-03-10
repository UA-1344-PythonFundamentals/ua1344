even_div2 = []  
odd_div3 = []   
not_div2_3 = [] 

for num in range(1, 11):
    if num % 2 == 0:  
        even_div2.append(num)
    elif num % 3 == 0:  
        odd_div3.append(num)
    else:  
        not_div2_3.append(num)

print("Even numbers divisible by 2:", even_div2)
print("Odd numbers divisible by 3:", odd_div3)
print("Numbers not divisible by 2 and 3:", not_div2_3)        