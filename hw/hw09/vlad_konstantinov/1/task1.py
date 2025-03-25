import random

x = random.randint(0, 100)

tries = 0
while tries < 10:
    y = int(input("Enter a number: "))
    if y == x:
        print("Well, well, you did it!")
        break
    elif y < x:
        print("Your guess is too low. Try again!")
    elif y > x:
        print("Your guess is too high. Try again!")
    tries += 1
else:
    print(f"You lose! The correct number was {x}.")
