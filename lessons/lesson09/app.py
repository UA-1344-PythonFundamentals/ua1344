import pygame
from colors import Colors


pygame.init()


gameDisplay = pygame.display.set_mode((800,600)) 
pygame.display.set_caption('My first game')

font = pygame.font.SysFont('Calibri', 25, True, False)


is_running = True


FPS = 30

clock = pygame.time.Clock()

POINTTS = []

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            
            print("User pressed a key.", event)
        elif event.type == pygame.KEYUP:
            print("User let go of a key.", event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            key =  event.dict
            if key['button'] == 1:
                POINTTS.append(key['pos'])
            elif key['button'] == 3:
                if len(POINTTS) > 0:
                    POINTTS.pop()


    gameDisplay.fill(Colors.White)

   
    if len(POINTTS) > 2:
        pygame.draw.polygon(gameDisplay, Colors.Blue, POINTTS, width=0)
    for point in POINTTS:
        pygame.draw.circle(gameDisplay, Colors.Red, point, 5, 0)
        text = font.render(f"{point}",True, Colors.Black)
        gameDisplay.blit(text, (point[0]-50, point[1] - 30))





    pygame.display.update()
    clock.tick(FPS)
