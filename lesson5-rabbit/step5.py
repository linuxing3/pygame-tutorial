# 1 - 导入库
import pygame
from pygame.locals import *
import math
import random

# 2 - 初始化游戏，主要是设置一些变量
pygame.init()

# 2.1 屏幕尺寸 
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 自定义上下左右键为awsd
keys = [False, False, False, False]
# 玩家定位
playerpos = [100, 100]
# 发射点
acc = [0, 0]
# 弓箭库，放置弓箭
arrows = []
# 敌人计时器
badtimer = 100
badtimer_current = 0
# 存储每个敌人的位置
badguys = [[640, 100]]
# 健康值
healthvalue = 194

# 初始化混音器
pygame.mixer.init()

# 3 - 加载图片作为游戏的元素
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")

# 3.1 - 加载声音
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
# 开始播放背景音乐
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# 4 - 开始游戏画面的循环播放
# 运行状态，1就运行，0就停止
running = 1
# 退出码，1就退出 0 就运行
exitcode = 0

# 开始游戏
while running:
    # 启动计时器，开始倒计时
    badtimer -= 1

    # 5 - 清除屏幕，准备画出元素
    screen.fill(0)

    # 6 - 画出元素图标，位置 X:100, Y:100
    for x in range(int(SCREEN_WIDTH/grass.get_width())+1):
        for y in range(int(SCREEN_HEIGHT/grass.get_height())+1):
            screen.blit(grass, (x*100, y*100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # 6.1 - 设置位置和移动
    position = pygame.mouse.get_pos()
    # 注意这里使用的atan2函数，是一个三角函数，用来计算转动角度的
    angle = math.atan2(position[1]-(playerpos[1]+32),
                       position[0]-(playerpos[0]+26))
    # 使用transform的rotate，进行旋转
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2,
                  playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - 射箭, bullet = [ 角度, 下一横坐标速度， 下一纵坐标速度 ]
    for bullet in arrows:
        # 这里的index是arrows的索引
        index = 0
        # 通过三角函数的sin和cos，计算x和y方向的速度
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        # 子弹的x方向进行移动，y方向进行移动
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            # 子弹发射前进行旋转
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            # 发射到指定方向和位置
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 - 敌人
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        # 减少计时器
        badtimer = 100-(badtimer_current*2)
        if badtimer_current >= 35:
            badtimer_current = 35
        else:
            badtimer_current += 5

    # 这里的index是badguys的坐标的索引
    index_badguy = 0
    for badguy in badguys:
        if badguy[0] < -64:
            # 根据索引删除
            badguys.pop(index_badguy)
        badguy[0] -= 7
        # 6.3.1 - 撞击行为
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5, 20)
            badguys.pop(index_badguy)

        # 6.3.2 - 检查撞击
        index_arrow = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index_badguy)
                arrows.pop(index_arrow)
            index_arrow += 1
        # 6.3.3 - 下一个badguy
        index_badguy += 1
    # 再次循环，画出敌人
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6.4 - 时钟
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str(
        (90000-pygame.time.get_ticks())/1000 % 60).zfill(2), True, (0, 0, 0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]
    screen.blit(survivedtext, textRect)

    # 6.5 - 健康栏，显示健康值
    screen.blit(healthbar, (5, 5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8, 8))

    # 7 - 刷新屏幕
    pygame.display.flip()

    # 8 - 事件循环
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32), position[0] -
                                      (playerpos1[0]+26)), playerpos1[0]+32, playerpos1[1]+32])

    # 9 - 控制玩家位置
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

    # 10 - 检查胜负
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0]*1.0/acc[1]*100
    else:
        accuracy = 0

# 11 - 运行状态下，显示胜负结果，显示画面
if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0, 0))
    screen.blit(text, textRect)

# 任何情况下，按退出键就结束
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
