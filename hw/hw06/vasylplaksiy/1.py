#task 1

workList = range(1, 11)
evenBy2 = []
oddBy3 = []
notDivisibleBy2and3 = []

for i in workList:
    if i % 2 == 0: evenBy2.append(i)
    if i % 2 != 0 and i % 3 == 0: oddBy3.append(i)
    if i % 2 != 0 and i % 3 != 0: notDivisibleBy2and3.append(i)

print("#task 1")
print("1-10 even by 2", evenBy2)
print("1-10 odd by 3", oddBy3)
print("1-10 not divisible by 2 and 3", notDivisibleBy2and3)


print("#task 2")
while True:
    login = input("Login: ")
    if login == "First":
        print(f"Hello {login}!")
        break
    else:
        print("Error! Try again")