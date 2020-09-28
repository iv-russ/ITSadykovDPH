#Б02-010 Садыков Даниил

import pygame
from pygame.draw import *



pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 200; y1 = 200
x2 = 150; y2 = 170
x3 = 250; y3 = 170

rect(screen, (255,255,255), (0, 0, 400, 400))
circle(screen, (255,255,0), (x1, y1), 100)
circle(screen, (255,0,0), (x2,y2), 20)
circle(screen, (255,0,0), (x3,y3), 15)
circle(screen, (0,0,0), (x2,y2), 10)
circle(screen, (0,0,0), (x3,y3), 10)

rect(screen, (0,0,0), (150, 250, 100, 20))

polygon(screen, (0,0,0), [(100, 130), (115,115), (195, 155), (180, 170)])
polygon(screen, (0,0,0), [(285, 110), (300, 120), (215, 180), (205, 170)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
