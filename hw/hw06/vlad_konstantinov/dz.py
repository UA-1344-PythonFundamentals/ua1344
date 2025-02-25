num_d = []
num_od = []
num_no = []

for i in range(1,11):
    if i % 2 == 0:
        num_d.append(i)
    if i % 3 == 0:
        num_od.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        num_no.append(i)

print(f"\nEven numbers divisible by 2: {num_d}")
print(f"Odd numbers divisible by 3: {num_od}")
print(f"Numbers not divisible by 2 or 3: {num_no}")



while True:
    user = str(input())
    if (user == "First"):
        print(f"hello")
        break
    else:
        print("Error")
        continue