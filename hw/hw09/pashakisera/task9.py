import random

def guess_the_number():
    while True:
        secret_number = random.randint(1, 100)
        attempts = 10

        print("\nI have chosen a number between 1 and 100. You have 10 attempts to guess it.")

        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}. Enter your guess: "))

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                if guess < secret_number:
                    print("My number is higher.")
                elif guess > secret_number:
                    print("My number is lower.")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
                    break
            except ValueError:
                print("Please enter only numbers.")

        else:
            print(f"You've used all 10 attempts. The number was {secret_number}.")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! See you next time!")
            break


guess_the_number()