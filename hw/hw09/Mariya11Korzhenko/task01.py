from random import randint

def guess_number():
    attemts = 10
    magic_number = randint(0, 100)

    while attemts != 0:
        entered_number = int(input("Try to guess entered number: "))
        if(entered_number == magic_number):
            print (f"You have guessed a number, it is {entered_number}!!!")
            break
        else:
            if(entered_number > magic_number):
                print(f"Entered number {entered_number} is bigger that number to guess")
            else:
                print(f"Entered number {entered_number} is less that number to guess")
        attemts -=1
    if(attemts == 0):
        print("You have tried all 10 tries. Good Bye!")

guess_number()



