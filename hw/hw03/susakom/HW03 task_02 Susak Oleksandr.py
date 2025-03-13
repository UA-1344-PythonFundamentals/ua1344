# HW_3 Susak Oleksandr
task_value = 4931
separate_symblos=list(str(task_value))
var1, var2, var3, var4 = separate_symblos
result_part1= int(var1)*int(var2)*int(var3)*int(var4)
print("Result product=",result_part1)
reversed_value = int(str(task_value)[::-1]) 
print("Reserse number=", reversed_value)
digits = sorted([int(d) for d in str(task_value)])
sorted_value=int("".join([str(d) for d in digits]))
# next variant is working too
# sorted_value=int("".join([str(d) for d in sorted([int(d) for d in str(task_value)])]))
print("Sorted_value=", sorted_value)