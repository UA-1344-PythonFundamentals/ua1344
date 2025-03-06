import random
randomNumber = random.randint(1, 100)
attempts = 10
print("You need to guess a number between 1 and 100")
for attempt in range(1, attempts + 1):
    while True:
        try:
            userNumber = int(input(f"Attempt {attempt} with {attempts}: Enter your number: "))
            
            if 1 <= userNumber <= 100:
                break
            else:
                print("Out of range! Please enter a number between 1 and 100.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if userNumber < randomNumber:
        print("Too low! Try again.")
    elif userNumber > randomNumber:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! The correct number was {userNumber}.")
        break

else:
    print(f"Game over! The correct number was {randomNumber}.")
