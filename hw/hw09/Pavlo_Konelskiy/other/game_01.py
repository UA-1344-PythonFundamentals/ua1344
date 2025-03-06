import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")

BLACK = (0, 0, 0)
RED = (255, 0, 0)

rect_x, rect_y = 50, 50
rect_size = 50

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_size, rect_size))
    pygame.display.update()

pygame.quit()