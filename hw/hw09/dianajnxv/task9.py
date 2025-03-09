import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess a number")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 30)

random_number = random.randint(1, 100)

user_input = ""
message = "Guess a number from 1 to 100"
running = True
attempts = 0
attempts_max = 10

while running:
    screen.fill(WHITE)

    message_surface = font.render(message, True, BLACK)
    screen.blit(message_surface, (50, 50))

    input_surface = font.render(user_input, True, BLACK)
    screen.blit(input_surface, (50, 150))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  
                if user_input.isdigit():
                    guess = int(user_input)
                    attempts += 1  

                    if guess == random_number:
                        message = f"Right! The number was {random_number}. Press Enter to restart."
                        user_input = ""
                        attempts = 0
                        random_number = random.randint(1, 100)  

                    elif attempts >= attempts_max:
                        message = f"Game over! The number was {random_number}. Press Enter to restart."
                        user_input = ""
                        attempts = 0
                        random_number = random.randint(1, 100)  

                    elif guess < random_number:
                        message = "Guessed number is greater"
                    else:
                        message = "Guessed number is less"

                else:
                    message = "Enter a valid number!"
                
                user_input = ""

            elif event.key == pygame.K_BACKSPACE:  
                user_input = user_input[:-1]

            elif event.unicode.isdigit():  
                user_input += event.unicode

pygame.quit()
