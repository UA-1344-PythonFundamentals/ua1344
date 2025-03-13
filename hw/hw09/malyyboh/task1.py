from random import randint


def guess_number():
    guess_num = randint(1, 100)
    user_attempts = 0
    print("Guess a number from 1 to 100, you have 10 attempts.")

    while user_attempts < 10:
        user_input = int(input("Please enter the number\n -> "))
        user_attempts += 1
        if user_input < guess_num:
            print("Guessed number is greater")
        elif user_input > guess_num:
            print("Guessed number is less")
        else:
            print("Congratulations, you guessed the number.")
            break
    else:
        print(
            "Sorry, but you have used 10 tries. You did not have time to guess the number."
        )


guess_number()
