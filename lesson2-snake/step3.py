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
pygame.display.set_caption('Snake Game by Daniel')
# 设置时钟
clock = pygame.time.Clock()
# 蛇长度和速度
snake_block = 10
snake_speed = 10

# 字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
#  画出蛇身体
def draw_our_snake(snake_block, snake_list):
    for block in snake_list:
        # block = [100, 100]
        pygame.draw.rect(dis, green, [block[0], block[1], snake_block, snake_block])
 
#  启动
def gameLoop():
    game_over = False
    game_close = False
    # #  开始位置在屏幕中央
    x1 = dis_width / 2
    y1 = dis_height / 2
    # # 记录位置的更改
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1

    while not game_over:
        # 
        # --------------------key event --------------------------------------
        # 
        while game_close == True:
            dis.fill(black)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # 
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    # 右移动
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # 
        # --------------------key event --------------------------------------
        # 

        # 计算将要移动到的位置 key left will cuase x1 = 300 - 10 = 290
        x1 = x1 + x1_change
        y1 = y1 + y1_change

        dis.fill(black)

        # # 生成一个蛇头
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # # 去掉第一个元素
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        # 画出蛇身体
        draw_our_snake(snake_block, snake_List)

        pygame.display.update()

        # 每循环一次，就画一个，如果不动，就会覆盖原地
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()