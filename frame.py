import pygame
import sys
from main import map,hero

M = map(10,10)
hero = hero(M)

WIN_WIDTH = 200
WIN_HEIGHT = 100
 
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
while not hero.win:

    p = hero.print()
    if p[0] == 0:
        pygame.draw.rect(sc, (255, 255, 255), (0, 0, 100, 100))
    elif p[0] == 1:
        pygame.draw.rect(sc, (0, 0, 0), (0, 0, 100, 100))
    elif p[0] == 2:
        pygame.draw.rect(sc, (255,20,147), (0, 0, 100, 100))
    elif p[0] == 3:
        pygame.draw.rect(sc, (p[1], 0, 0), (0, 0, 100, 100))
    elif p[0] == 4:
        pygame.draw.rect(sc, (255, 255, 0), (0, 0, 100, 100))
    if p[2] == 1:
        pygame.draw.rect(sc, (0, p[3], 0), (100, 0, 200, 100))
    else:
        pygame.draw.rect(sc, (p[3], p[3], 0), (100, 0, 200, 100))

    


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero.command(0)
            elif event.key == pygame.K_RIGHT:
                hero.command(1)

    pygame.display.update()
    clock.tick(60)