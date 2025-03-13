# HW09 Susak Oleksandr
import pygame
import sys
import random



pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("My_Pygame")

screen.fill(color='white')
font=pygame.font.Font('ariali.ttf', 20)
FONT_COLOR=(102, 158, 102)



random_value=random.randint(0, 100)

max_game_step=10
user_step = max_game_step
result=False
message = ""
user_input = " "
running = True

while running:

    screen.fill('white')
    start_text = font.render(f"You will have only {max_game_step} attempts to guess the number", True, FONT_COLOR)
    screen.blit(start_text, ((screen.get_width() - start_text.get_width()) / 2, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                user_step -= 1
                user_number = int(user_input)

                if user_number == random_value:
                    message = "My congratulations you are the winner!"
                    result=True
                elif user_step == 0:
                    message = "Game over. Unfortunately you lost."
                else:
                    if user_number > random_value:
                        message = f"Your number {user_number} is biggest that my."
                    else:
                        message = f"Your number {user_number} is smallest that my."
                    message += f"  You have {user_step} steps"
                user_input = ""
            else:
                user_input += event.unicode



    message_place = font.render(message, True, FONT_COLOR)

    input_surface = font.render(f"Your number is {user_input}", True, FONT_COLOR)

    screen.blit(message_place, ((screen.get_width() - message_place.get_width()) / 2, 150))

    screen.blit(input_surface, ((screen.get_width() - input_surface.get_width()) / 2, 100))

    pygame.display.flip()

    if result or user_step == 0:
        pygame.time.delay(3000)
        running = False