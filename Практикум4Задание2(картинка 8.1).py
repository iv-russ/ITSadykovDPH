#Б02-010 Садыков Даниил
import pygame
import math as m
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))


def draw_window(x, y, sizex, sizey):
    rect(screen, (230, 230, 255), (x, y, sizex, sizey))
    rect(screen, (64,234,255), (x+sizex*0.025, y+sizey*0.025, 0.45*sizex, 0.45*sizey))
    rect(screen, (64,234,255), (x+sizex*0.025, y+sizey*0.525, 0.45*sizex, 0.45*sizey))
    rect(screen, (64,234,255), (x+sizex*0.525, y+sizey*0.025, 0.45*sizex, 0.45*sizey))
    rect(screen, (64,234,255), (x+sizex*0.525, y+sizey*0.525, 0.45*sizex, 0.45*sizey))
    
    
    
    
def draw_a_cat(x, y, sizex, sizey):
    for i in range(6): #tail
        ellipse(screen, (0,0,0), [x+sizex/1.73+sizex*i/25-1, y+0.22*sizey+sizey*i/40-1, sizex/8.2+2 , sizey/2.7+2])
        ellipse(screen, (165,96,23), [x+sizex/1.73+sizex*i/25, y+0.22*sizey+sizey*i/40, sizex/8.2 , sizey/2.7])
    
    ellipse(screen, (0,0,0), [x+sizex/8-1, y-sizey/30-1, sizex/2+2 , 0.9*sizey+2]) #bodyline
    ellipse(screen, (165,96,23), [x+sizex/8, y-sizey/30, sizex/2 , 0.93*sizey]) #body
    
    ellipse(screen, (0,0,0), [x+sizex/15-1, y+0.43*sizey-1, sizex/12+2 , sizey/2.4+2]) #backpawline
    ellipse(screen, (165,96,23), [x+sizex/15, y+0.43*sizey, sizex/12 , sizey/2.4]) #backpaw
    
    ellipse(screen, (0,0,0), [x+sizex/7-1, y+0.7*sizey-1, sizex/7+2 , sizey/3.6+2]) #frontpawline
    ellipse(screen, (165,96,23), [x+sizex/7, y+0.7*sizey, sizex/7 , sizey/3.6]) #frontpaw
    
    ellipse(screen, (0,0,0), [x-1, y-1, sizex/4.2+2 , sizey/1.35+2], 1) #headline
    ellipse(screen, (165,96,23), [x, y, sizex/4.2 , sizey/1.35]) #head
    
    ellipse(screen, (0,0,0), [x+sizex/2.1-1, y+0.47*sizey-1, sizex/5.5+2, sizey/1.75+2]) #legbaseline
    ellipse(screen, (165,96,23), [x+sizex/2.1, y+0.47*sizey, sizex/5.5, sizey/1.75]) #legbase
    
    ellipse(screen, (0,0,0), [x+sizex/1.59-1, y+0.8*sizey-1, sizex/15+2 , sizey/2+2]) #legline
    ellipse(screen, (165,96,23), [x+sizex/1.59, y+0.8*sizey, sizex/15 , sizey/2]) #leg
    
    polygon(screen, (0,0,0), [(x+sizex/4.3 , y-0.1*sizey), (x+sizex/4.8, y+0.2*sizey), (x+sizex/6.3, y+0.05*sizey), (x+sizex/4.3 , y-0.1*sizey)]) #rightearline
    polygon(screen, (165,96,23), [(x+sizex/4.3-1 , y-0.1*sizey+1), (x+sizex/4.8-1, y+0.2*sizey-1), (x+sizex/6.3+1, y+0.05*sizey), (x+sizex/4.3-1 , y-0.1*sizey+1)]) #rightear
    polygon(screen, (255,157,122), [(x+sizex/4.44 , y-0.075*sizey), (x+sizex/4.95, y+0.135*sizey), (x+sizex/5.75, y+0.05*sizey), (x+sizex/4.44 , y-0.075*sizey)]) #rightearinterior
       
    polygon(screen, (0,0,0), [(x, y-0.1*sizey), (x+sizex/45, y+0.2*sizey), (x+sizex/13, y+0.05*sizey), (x, y-0.1*sizey)]) #leftearline
    polygon(screen, (165,96,23), [(x+1 , y-0.1*sizey+1), (x+sizex/45+1, y+0.2*sizey-1), (x+sizex/13-1, y+0.05*sizey), (x+1 , y-0.1*sizey+1)]) #leftear
    polygon(screen, (255,157,122), [(x+0.012*sizex , y-0.05*sizey), (x+sizex/38, y+0.135*sizey), (x+sizex/15.6, y+0.05*sizey), (x+0.012*sizex , y-0.05*sizey)]) #leftearinterior

    ellipse(screen, (0,0,0), [x+sizex/28-1, y-1+sizey/4, sizex/14.5+2 , sizey/4.2+2], 1) #lefteyeline
    ellipse(screen, (156,208,19), [x+sizex/28, y+sizey/4, sizex/14.5 , sizey/4.2]) #lefteye
    ellipse(screen, (0,0,0), [x+sizex/28+sizex/29, y+sizey/3.9, sizex/80 , sizey/4.6]) #lefteyelid
    ellipse(screen, (234,245,234), [x+sizex/28+sizex/100, y+sizey/3.7, sizex/35 , sizey/10]) #lefteyeshine
    
    ellipse(screen, (0,0,0), [x+sizex/7.2-1, y-1+sizey/4, sizex/14.5+2 , sizey/4.2+2], 1) #righteyeline
    ellipse(screen, (156,208,19), [x+sizex/7.2, y+sizey/4, sizex/14.5 , sizey/4.2]) #righteye
    ellipse(screen, (0,0,0), [x+sizex/7.2+sizex/29, y+sizey/3.9, sizex/80 , sizey/4.6]) #righteyelid
    ellipse(screen, (234,245,234), [x+sizex/7.2+sizex/100, y+sizey/3.7, sizex/35 , sizey/10]) #lefteyeshine
    
    polygon(screen, (0,0,0), [(x+sizex/8.4-sizex/80-1, y+sizey/2-1), (x+sizex/8.4+sizex/80+1, y+sizey/2-1), (x+sizex/8.4, y+sizey/1.8+1), (x+sizex/8.4-sizex/80-1, y+sizey/2-1)]) #nose
    polygon(screen, (255,157,155), [(x+sizex/8.4-sizex/80, y+sizey/2), (x+sizex/8.4+sizex/80, y+sizey/2), (x+sizex/8.4, y+sizey/1.8), (x+sizex/8.4-sizex/80, y+sizey/2)]) #nose
    
    
    line(screen, (0,0,0), (x+sizex/8.4, y+sizey/1.8), (x+sizex/8.4, y+sizey/1.6), 1) #linefromnoosetomouth
    arc(screen, (0,0,0), [x+sizex/8.4, y+sizey/1.75, sizex/40, sizey/12], 3.8, 6.28, 1) #rightmouthwing
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/44, y+sizey/1.75, sizex/40, sizey/12], 3.14, 6.28, 1) #leftmouthwing
    
    #whiskers(усы)
    #right
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/6.5, y+0.525*sizey, sizex/1.8, sizey*2], 1.25, 1.95, 1)
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/6.5+sizex/40, y+0.465*sizey, sizex/1.8, sizey*2], 1.35, 2.03, 1)
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/6.5-sizex/40, y+0.575*sizey, sizex/1.8, sizey*2], 1.15, 1.85, 1)
    
    #left
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/2.5, y+0.525*sizey, sizex/1.8, sizey*2], 1.25, 1.95, 1)
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/2.5-sizex/40, y+0.465*sizey, sizex/1.8, sizey*2], 1.15, 1.85, 1)
    arc(screen, (0,0,0), [x+sizex/8.4-sizex/2.5+sizex/40, y+0.575*sizey, sizex/1.8, sizey*2], 1.35, 2.05, 1)
    
    
def ball_of_thread(x, y, r):
    circle(screen, (0,0,0), (x,y), r+1)
    circle(screen, (154,154,154), (x,y), r)
    arc(screen, (0,0,0), [x-r-0.17*r, y-r+0.25*r, 1.9*r, 1.9*r], 0, 1.66, 1)
    arc(screen, (0,0,0), [x-r-0.35*r, y-r+0.35*r, 2*r, 2*r], 0, 1.66, 1)
    arc(screen, (0,0,0), [x-r-0.45*r, y-r+0.45*r, 2*r, 2*r], 0, 1.66, 1)
    arc(screen, (0,0,0), [x-r+0.25*r, y-r+0.5*r, 2*r, 2*r], 2, 3, 1)
    arc(screen, (0,0,0), [x-r+0.41*r, y-r+0.65*r, 2.1*r, 2.1*r], 2, 3, 1)
    arc(screen, (0,0,0), [x-r+0.65*r, y-r+0.85*r, 2*r, 2*r], 2, 3, 1)
    
    #threadtail
    arc(screen, (154,154,154), [x-0.95*r, y+0.225*r, 0.7*r, 0.7*r], 4.1888, 5.236, 1)
    
    arc(screen, (154,154,154), [x-0.95*r-0.35*r, y+0.225*r+0.606*r, 0.7*r, 0.7*r], 1.0472, 2.11, 1)
    
    arc(screen, (154,154,154), [x-0.95*r-0.7*r, y+0.225*r, 0.7*r, 0.7*r], 4.1888, 5.236, 1)
    
    arc(screen, (154,154,154), [x-0.95*r-1.05*r, y+0.225*r+0.606*r, 0.7*r, 0.7*r], 1.0472, 2.11, 1)
    
    arc(screen, (154,154,154), [x-0.95*r-1.4*r, y+0.225*r, 0.7*r, 0.7*r], 4.1888, 5.236, 1)
    
    arc(screen, (154,154,154), [x-0.95*r-1.75*r, y+0.225*r+0.606*r, 0.7*r, 0.7*r], 1.0472, 2.11, 1)
    
    
rect(screen, (105,66,12), (0, 400, 600, 400))
rect(screen, (84,54,5), (0, 0, 600, 400))


draw_window(300, 25, 250, 350)
draw_a_cat(60, 400, 600, 180)
ball_of_thread(400, 660, 60)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
