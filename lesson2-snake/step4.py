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
letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 显示模式
dis = pygame.display.set_mode((dis_width, dis_height))
# 设置标题
pygame.display.set_caption('Snake Game by Edureka')
# 设置时钟
clock = pygame.time.Clock()
# 蛇长度和速度
snake_block = 10
snake_speed = 10

# 字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
block_font = pygame.font.SysFont("comicsansms", 10)
 
# 显示得分
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
#  画出蛇身体
# snake_list = [[100, 100], [ 100, 102 ], [ 100, 103 ]]
def our_snake(snake_block, snake_list):
    i = 0
    for block in snake_list:
        pygame.draw.rect(dis, red, [block[0], block[1], snake_block, snake_block])
        letter_snake(letters_list[i], block )
        i = i + 1

def letter_snake(letter, position):
    value = block_font.render(letter, True, yellow)
    dis.blit(value, position)
 
# 显示消息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
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
 
    snake_List = []
    Length_of_snake = 1
    #  目标的位置
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        # 
        # --------------------key event --------------------------------------
        # 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
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
                    # 左移动
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
 
        #  超出屏幕就退出
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # 将要移动到的位置
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        # 画出目标
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        # 蛇头
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        # 假如蛇头到蛇身体
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        # 画出蛇身体
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        # 如果蛇身体碰到目标，蛇身长一寸
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # 蛇身的长度增加
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()