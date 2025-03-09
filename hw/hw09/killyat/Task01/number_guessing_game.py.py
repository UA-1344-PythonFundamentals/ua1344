import random
#code

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Вгадайте число від 1 до 100. У вас є 10 спроб!")

    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"Спроба {attempts}/{max_attempts}. Введіть ваше число: "))
            
            if guess == secret_number:
                print(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб!")
                return
            elif guess < secret_number:
                print("Число більше, ніж ваше вгадування.")
            else:
                print("Число менше, ніж ваше вгадування.")
            
            print(f"Залишилося спроб: {max_attempts - attempts}")
        except ValueError:
            print("Будь ласка, введіть коректне число.")
            continue

    print(f"На жаль, спроби вичерпані. Секретне число було {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()