# HW_06 Susak Oleksandr
task_06 = range(1, 11)
even_numbers=[]
odd_numbers=[]
other_numbers=[]
for i in task_06:
    if i%2 == 0:
        even_numbers.append(i)
for i in task_06:
    if i%3 == 0:
        odd_numbers.append(i)
for i in task_06:
    if i%2 == 0 or i%3 == 0:
        pass
    else:
        other_numbers.append(i)
print("even_numbers=", even_numbers)
print("odd_numbers=", odd_numbers)
print("other_numbers=", other_numbers)


correct_login = "First"
while True:
    user_login = input("Enter you login: ")
    if user_login == correct_login:
        print("Hello, First!")
        break 
    else:
        print("Error. Please take again")
