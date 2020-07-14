import pygame
import time
import random
 
pygame.init()

# 颜色设置
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# 显示吃准 
dis_width = 600
dis_height = 400
# 显示模式
dis = pygame.display.set_mode((dis_width, dis_height))
# 设置标题
pygame.display.set_caption('Snake Game by Edureka')
clock = pygame.time.Clock()
snake_speed = 10

#  启动
def gameLoop():
    game_over = False
    game_close = False

    #  开始位置在屏幕中央
    x1 = dis_width / 2
    y1 = dis_height / 2
    # 记录位置的更改
    x1_change = 0
    y1_change = 0
    snake_List = [[100, 100], [ 100, 120 ], [ 100, 140 ]]

    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        dis.fill(black)
        # 画出目标
        pygame.draw.rect(dis, green, [100, 100, 20, 20])

        # 蛇头
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        # 假如蛇头到蛇身体
        snake_List.append(snake_Head)

        for i in snake_List:
            pygame.draw.rect(dis, red, [i[0], i[1], 20, 20])
 
        pygame.display.update()
        clock.tick(snake_speed)

 
    pygame.quit()
    quit()
 
 
gameLoop()