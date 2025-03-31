import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Генеруємо випадкове число від 1 до 100
    attempts = 10  # Кількість спроб

    print("Я загадав число від 1 до 100. У тебе є 10 спроб, щоб його відгадати!")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}: Введи своє число: "))
            
            if guess < 1 or guess > 100:
                print("Будь ласка, введи число в діапазоні від 1 до 100.")
                continue

            if guess == number_to_guess:
                print(f"Вітаю! Ти вгадав число {number_to_guess} за {attempt} спроб(у)!")
                return
            elif guess < number_to_guess:
                print("Моє число більше!")
            else:
                print("Моє число менше!")
        
        except ValueError:
            print("Будь ласка, введи ціле число!")

    print(f"На жаль, ти не вгадав. Загадане число було {number_to_guess}.")

# Запускаємо гру
number_guessing_game()
