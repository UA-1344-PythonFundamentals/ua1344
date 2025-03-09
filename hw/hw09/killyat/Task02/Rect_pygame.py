import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Прямокутник у межах вікна")

RECT_COLOR = (255, 0, 0)
RECT_WIDTH = 100
RECT_HEIGHT = 50

rect_x = WINDOW_WIDTH // 2 - RECT_WIDTH // 2
rect_y = WINDOW_HEIGHT // 2 - RECT_HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255)) 
    pygame.draw.rect(window, RECT_COLOR, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))

    pygame.display.flip()

pygame.quit()