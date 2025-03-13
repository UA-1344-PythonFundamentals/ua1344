from random import randint

tries = 10
number = randint(1, 100)

while tries > 0:
    guess = int(input("Guess the number between 1 and 100. You have 10 tries: "))
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number:
        print("The number is greater than your guess. Tries left:", tries - 1)
    else:
        print("The number is smaller than your guess. Tries left:", tries - 1)
    tries -= 1
else:
    print(f"You didn't guess the number. The number was {number}.")