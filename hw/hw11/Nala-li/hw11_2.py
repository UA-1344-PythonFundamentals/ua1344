def get_day_of_week(day_number):
    """Функція повертає день тижня за номером."""
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "Пʼятниця",
        6: "Субота",
        7: "Неділя"
    }

    # Перевіряємо, чи є такий день
    if day_number < 1 or day_number > 7:
        return "Помилка: число повинно бути від 1 до 7."

    return days.get(day_number)


def main():
    try:
        # Вводимо число
        day_input = input("Введіть номер дня тижня (від 1 до 7): ")

        # Перетворюємо введене значення на ціле число
        day_number = int(day_input)

        # Отримуємо день тижня за числом
        result = get_day_of_week(day_number)
        print(result)

    except ValueError:
        print("Помилка: введено не число.")


# Запуск головної функції
main()