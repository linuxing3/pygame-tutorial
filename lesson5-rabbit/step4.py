# Ratate the player
# 1 - Import library
import pygame
import math
import random
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys=[False, False, False, False]
playerpos=[100, 100]

acc=[0,0]
arrows=[]

# 定义了一个定时器，使得游戏里可以经过一段时间后就新建一只獾。
badtimer=100
badtimer_current=0
badguys=[[640,100]]
healthvalue=194

# 3 - Load images
player = pygame.image.load("assets/fugu.png")
grass = pygame.image.load("assets/fugu.png")
arrow = pygame.image.load("assets/spr_missile_half.png")

badguyimg1 = pygame.image.load("assets/spr_missile.png")
badguyimg=badguyimg1
healthbar = pygame.image.load("assets/spr_missile.png")
health = pygame.image.load("assets/spr_missile.png")

running = True
# 4 - keep looping through
while running:
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
        if event.type==pygame.MOUSEBUTTONDOWN:
            # 当玩家点击鼠标，就需要射出一支箭头。
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrawangle = math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26))
            arrows.append([arrawangle, playerpos1[0]+32,playerpos1[1]+32])

    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0

    # 
    badtimer -= 1
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
    # screen.blit(player, playerpos)

    # 6.1 player transform with atan2
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(player, playerpos1)


    # 6.2 - Draw arrows
    # vely和velx的值是根据三角定理算出来的。
    # 10是箭头的速度。if表达式是检查箭头是否超出了屏幕范围，如果超出，就删除这个箭头。
    # 第二个for表达式是循环来把箭头根据相应的旋转画出来。
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # blit castle
    # screen.blit(castle, (0, 30))
    # screen.blit(castle, (0, 135))
    # screen.blit(castle, (0, 240))
    # screen.blit(castle, (0, 345))

    # 计时器
    if badtimer == 0:
        badguys.append([640, random.randint(50,430)])
        # 这里是倒计时的实现，最大为100，每次降低一个单位
        battimer = 100 - (badtimer_current * 2)
        # 当前时刻每次加5，不超过35
        if badtimer_current >= 75:
            badtimer_current = 75
        else:
            badtimer_current+=5
    index = 0
    # move 
    for badguy in badguys:
        if badguy[0]<0:
            badguys.pop(index)
        # 向左移动
        badguy[0]-=7
        index+=1
    # draw badguys
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    # 6.5 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))

    if exitcode==0:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(gameover, (0,0))
        screen.blit(text, textRect)
    else:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(youwin, (0,0))
        screen.blit(text, textRect)
    # 7 - update the screen
    pygame.display.flip()

