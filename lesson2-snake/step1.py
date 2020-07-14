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
clock = pygame.time.Clock()
# 设置标题
pygame.display.set_caption('Snake Game by Edureka')
 
#  启动
def gameLoop():
    game_over = False
    game_close = False

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
        pygame.draw.rect(dis, red, [200, 200, 20, 20])
 
        pygame.display.update()

 
    pygame.quit()
    quit()
 
 
gameLoop()