def enter_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від’ємним!")
    if age % 2 == 0:
        print(f"Ваш вік ({age}) є парним числом.")
    else:
        print(f"Ваш вік ({age}) є непарним числом.")

def main():
    try:
        age = int(input("Введіть ваш вік: "))
        enter_age(age)
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()