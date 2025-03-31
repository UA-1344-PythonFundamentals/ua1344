class NegativeAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise NegativeAgeError("Вік не може бути від'ємним.")

    if age % 2 == 0:
        return "Ваш вік парний."
    else:
        return "Ваш вік не парний."


def main():
    try:
        age = int(input("Введіть вік: "))

        result = check_age(age)
        print(result)

    except ValueError:
        print("Помилка, введено не число.")
    except NegativeAgeError as e:
        print(f"Помилка: {e}")


main()