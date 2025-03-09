import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("You have 10 attempts to guess a number between 1 and 100.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/10 - Enter your number: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            return

    print(f"You've lost. You've used all 10 attempts. The correct number was {secret_number}.")

guess_number_game()
