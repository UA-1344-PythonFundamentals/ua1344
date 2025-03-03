import pygame
from random import randint
from colors import Colors


pygame.init()
HEIGHT = 600
WIDTH = 800

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")


is_running = True
FPS = 10

clock = pygame.time.Clock()

tank = [50, 300]

target = [WIDTH - 50, 300]
piu = []


def move_target(target, target_step=5):
    if randint(0, 1) == 0:
        target[1] = target[1] + target_step
    else:
        target[1] = target[1] - target_step


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            key = event.dict
            if key["key"] == 1073741906:
                tank[1] = tank[1] - 5
            elif key["key"] == 1073741903:
                tank[0] = tank[0] + 5
            elif key["key"] == 1073741905:
                tank[1] = tank[1] + 5
            elif key["key"] == 1073741904:
                tank[0] = tank[0] - 5
            if key["key"] == 32:
                piu.append([tank[0] + 30, tank[1]])
            print("User pressed a key.", event)
        elif event.type == pygame.KEYUP:
            print("User let go of a key.", event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            key = event.dict

    gameDisplay.fill(Colors.White)
    move_target(target)

    pygame.draw.rect(
        gameDisplay, Colors.Black, (target[0] - 25, target[1] - 25, 10, 30), 0
    )
    # tank
    pygame.draw.rect(gameDisplay, Colors.Black, (tank[0] - 25, tank[1] - 25, 30, 30), 0)
    pygame.draw.rect(gameDisplay, Colors.Black, (tank[0] + 5, tank[1] - 12, 10, 3), 0)

    #
    for i in range(len(piu)):
        pygame.draw.circle(gameDisplay, Colors.Gray, piu[i], 3, 0)
        piu[i][0] = piu[i][0] + 10
    for i in range(len(piu)):
        if piu[i][0] > WIDTH:
            piu.pop(i)

    pygame.display.update()
    clock.tick(FPS)
 