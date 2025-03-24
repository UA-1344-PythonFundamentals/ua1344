import pygame
import sys
from random import randint

class Colors:
    Aqua = (0, 255, 255)
    Black = (0, 0, 0)
    Blue = (0, 0, 255)
    Fuchsia = (255, 0, 255)
    Gray = (128, 128, 128)
    Green = (0, 128, 0)
    Lime = (0, 255, 0)
    Maroon = (128, 0, 0)
    NavyBlue = (0, 0, 128)
    Olive = (128, 128, 0)
    Purple = (128, 0, 128)
    Red = (255, 0, 0)
    Silver = (192, 192, 192)
    Teal = (0, 128, 128)
    White = (255, 255, 255)
    Yellow = (255, 255, 0)

pygame.init()

gameDisplay = pygame.display.set_mode((700, 350)) 
pygame.display.set_caption('Guess the number ;)')
clock = pygame.time.Clock()

FPS = 30
is_running = True

NUMBER = randint(0,100)
attempts = 10
msg1 = "Guess the number between 1 and 100."
font1 = pygame.font.SysFont('Calibri', 35, True, False)

msg2 = f"Attempts: {attempts}"
font2 = pygame.font.SysFont('Calibri', 25, True, False)

guess = ""
color3 = Colors.Black

def compare_numbers(x, y):
    if x > y:
        return (False, f"{x} is too big")
    elif x < y:
        return (False, f"{x} is too small")
    else:
        return (True, f"{x} equals {y}")


while is_running:
    gameDisplay.fill(Colors.Teal)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if str(event.unicode).isdigit():
                guess += event.unicode
            if event.key == pygame.K_RETURN:
                attempts -= 1
                result = compare_numbers(int(guess), NUMBER)
                msg2 = f"Attempts: {attempts}" + " "*15 + result[1]
                if result[0]:
                    guess = "CONGRATULATION! YOU WIN!"
                    color3 = Colors.Lime
                    is_running = False
                elif attempts == 0:
                    guess = "Sorry, you've lost..."
                    color3 = Colors.Red
                    is_running = False
                else:
                    guess = ""
   

    label1 = font1.render(msg1,True, Colors.Maroon)
    gameDisplay.blit(label1, (60, 30))
    label2 = font2.render(msg2, True, Colors.Black)
    gameDisplay.blit(label2, (60, 80))
    label3 = font2.render(guess, True, color3)
    gameDisplay.blit(label3, (250, 150))
    

    pygame.display.update()
    if not is_running:
        pygame.time.wait(2500)
    clock.tick(FPS)

