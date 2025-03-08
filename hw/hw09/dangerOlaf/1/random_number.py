# Write a game script that randomly generates a number from a range of 1 to 100 
# and asks the user to guess that number in 10 tries.

from random import randint as rand

num = rand(1,100)

for i in range(0,11):
    if i != 10:
        entered = int(input("Please enter your number: "))
        if num == entered: 
            print("Congratulations, you guessed the number, it's", str(num))
            break
        elif entered > num: print("Your entered number greater, than the random")
        else: print("Your entered number less, than the random")
    else: print("Unfortunately, you didn't guess the number")
