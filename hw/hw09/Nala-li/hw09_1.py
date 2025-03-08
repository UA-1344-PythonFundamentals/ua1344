import random
secret_number = random.randint(1, 100)

print("Вітаю у грі 'Вгадай число'!")
print("Я загадала число від 1 до 100. У тобе 10 спроб вгадати його.")


for attempt in range(1, 11):
    guess = int(input(f"Спроба {attempt}: Введи число: "))

    if guess < secret_number:
        print("Моє число більше!")
    elif guess > secret_number:
        print("Моє число меньше!")
    else:
        print(f"Вітаю! Ти вгадав число {secret_number} з {attempt}-ої спроби!")
        break
else:
    print(f"Ти використав всі спроби. Моє число було {secret_number}.Спробуй ще.")