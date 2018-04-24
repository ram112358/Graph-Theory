import sys
import pygame
import DisplayTesterFunctions

pygame.init()

n, m = raw_input("How big do you want the board (n,m)>2:").split()
n=int(n)
m=int(m)

screen = DisplayTesterFunctions.setup(n,m)
DisplayTesterFunctions.drawboard(screen, n,m)
DisplayTesterFunctions.refresh()
r = raw_input("")
