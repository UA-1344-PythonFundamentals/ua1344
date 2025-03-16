from random import randint

guessNumber = randint(1, 100)
attempts = 10

while attempts > 0:
    userGuess = int(input(f"Guess the number from 1 to 100, You have {attempts} attempts. Your guess is: "))
    if userGuess == guessNumber:
        print("WIN!!!")
        break
    elif userGuess > guessNumber:
        print("try lower")
    else:
        print("try higher")
    attempts -= 1
else:
    print("You lose!")

