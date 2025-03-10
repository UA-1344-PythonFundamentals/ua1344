import random

guess_to_number = random.randint(1, 100)

attempts = 10

guess = None

print("Вітаю у грі! Вгадай число від 1 до 100!")

while attempts > 0:
    guess = int(input(f"Залишилось {attempts} спроб. Введіть число: "))

    if guess == guess_to_number:
        print("Вітаю з перемогою!")
        break
    elif guess < guess_to_number:
        print("Загадане число більше")
    elif guess > guess_to_number:
        print("Загадане число менше")

    attempts -= 1

if attempts == 0 and guess != guess_to_number:
    print(f"На жаль, ви не вгадали число. Правильна відповідь {guess_to_number}")



