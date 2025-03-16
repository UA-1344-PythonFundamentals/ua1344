def get_weekday(number):
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П’ятниця",
        6: "Субота",
        7: "Неділя"
    }

    if number in days:
        print(f"Числу {number} відповідає дню тижня: {days[number]}")
    else:
        print("Помилка: Введене число має бути від 1 до 7.")


def main():
    try:
        number = int(input("Введіть число (1-7): "))
        get_weekday(number)
    except ValueError:
        print("Помилка: Будь ласка, введіть ціле число.")


if __name__ == "__main__":
    main()