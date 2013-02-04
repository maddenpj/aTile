import pygame
import sys
from pygame.locals import *
from Grid import Grid


window = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Tile Game')
screen = pygame.display.get_surface()
pygame.key.set_repeat(1,50)


grid = Grid(100, 100, 500, 500, 0.90)

while True:
    screen.fill((1,1,1,0))
    grid.draw(pygame, screen)
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                grid.click(e.pos)
