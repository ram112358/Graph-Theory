import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)

CELL_SIZE = 60
LINE_WIDTH = 10

def setup(n,m):
    pygame.init()
    screen = pygame.display.set_mode(((CELL_SIZE*m+LINE_WIDTH),(CELL_SIZE*n+LINE_WIDTH)))
    screen.fill(WHITE)
    return screen

def refresh():
    pygame.display.update()

def drawboard(screen, n,m):
    for i in range(0,(CELL_SIZE*m+LINE_WIDTH)):
        if i%6 == 0:
            pygame.draw.lines(screen, BLACK, 0, [(0,i),(CELL_SIZE*n+LINE_WIDTH,i)], LINE_WIDTH)
        # else:
        #     for j in range(0,(6*n+1)*10):
