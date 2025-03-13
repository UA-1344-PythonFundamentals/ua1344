for num in range(1, 11):
    if num % 2 == 0:
        print(f"even_div_by_2: {num}")
    elif num % 2 != 0 and num % 3 == 0:
        print(f"odd_div_by_3: {num}")
    else:
        print(f"not_div_by_2_3: {num}")

while True:
    login = input("Введіть логін: ")

    if login == "First":
        print("Привіт, First!")
        break
    else:
        print("Error")