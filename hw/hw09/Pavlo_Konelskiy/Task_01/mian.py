import random

target_number = random.randint(1, 100)

attempts = 10

print("Guess the number between 1 and 100. You have 10 tries!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}/{attempts}: Enter you guess:"))

    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempt} attempts!")
        break

else:
    print(f"Sorry, you used all attempts. The number was {target_number}.")
    
