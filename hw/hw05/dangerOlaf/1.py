#Create a list that contains elements of integer type, 
#then use the loop to change the type of these elements to a floating type.

the_list = [1, 4, 7, 8, 9, 23, 565]
for i in range(len(the_list)):
    the_list[i] = float(the_list[i])

print(the_list)