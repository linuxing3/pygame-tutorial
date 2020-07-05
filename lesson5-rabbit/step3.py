# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys=[False, False, False, False]
playerpos=[100, 100]

# 3 - Load images
player = pygame.image.load("assets/fugu.png")
grass = pygame.image.load("assets/fugu.png")
castle = pygame.image.load("assets/spr_missile.png")


# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    if keys[0]:
        playerpos[1]-=5
    if keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    if keys[3]:
        playerpos[0]+=5

    # 6 - draw the screen elements
    screen.blit(player, playerpos)

    # blit castle
    # screen.blit(castle, (0, 30))
    # screen.blit(castle, (0, 135))
    # screen.blit(castle, (0, 240))
    # screen.blit(castle, (0, 345))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
