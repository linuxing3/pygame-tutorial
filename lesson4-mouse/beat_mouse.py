import pygame
import sys
import random
from pygame.locals import *  # 引入鼠标事件类型

pygame.init()  # 初始化
window = pygame.display.set_mode([600, 400])  # 设定窗口

sur = pygame.Surface([600, 400])  # 绘制背景容器
clr = (0, 0, 255)
posAll = [[100, 150], [300, 150], [500, 150], [
    200, 300], [400, 300]]  # 六个位置
rad = 50
tick = 0  # 计数器
pos = posAll[0]  # 外面记录圆的位置

# 分数
score = 0  # 分数计数
pygame.font.init()  # 初始化文字
score_font = pygame.font.Font(None, 30)  # ！！设定字体和字号
score_sur = score_font.render(str(score), False, (255, 0, 0))  # ！！生成计数表面

# 鼠标
pygame.mouse.set_visible(False)  # !!隐藏鼠标
mpos = [300, 200]  # !!记录鼠标位置

times = 0  # 地鼠跳出的次数
times_max = 10  # 最多次数
tick_max = 30  # 地鼠每次跳多少帧
map = pygame.image.load('resources/images/fugu.png')  # ！！读取图片

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:  # 如果是鼠标按下事件
            dis = pygame.math.Vector2(
                mpos[0]-pos[0], mpos[1]-pos[1])  # 计算坐标差
            len = pygame.math.Vector2.length(dis)  # 计算距离
            if len < rad:
                tick = 1000  # 立即变换位置
                score = score+1  # 计分增加
        elif event.type == MOUSEMOTION:  # 当鼠标移动的时候
            mpos = pygame.mouse.get_pos()  # 更新鼠标位置

    if times >= times_max:
        # 显示结束画面
        sur.fill((0, 0, 0))  # ！！结束时候仍然用黑色清空画面
        pygame.mouse.set_visible(True)
        end_font = pygame.font.Font(
            None, 48)  # ！！设定字体和字号
        end_sur = score_font.render(
            "你的分数是:{}/{}！".format(score, times_max), True, (255, 0, 0))  # ！！生成计数表面
        window.blit(sur, (0, 0))
        window.blit(end_sur, (100, 100))  # 增加分数表面
    else:
        sur.blit(map, (0, 0))  # ！！添加背景图片
        # 每帧循环执行的代码
        if tick > tick_max:  # 每50次刷新变换一次
            times = times+1  # 增加计次
            score_sur = score_font.render(
                "分数:{}/{}！".format(score, times), False, (255, 0, 0))  # 重新生成分数文字表面
            a = random.randint(0, 4)  # 随机0到4
            pos = posAll[a]  # 更新外部记录的圆的位置
            tick = 0  # 重置计数器
        else:  # 不刷新变换的时候
            tick = tick+1  # 增加计数器

        # 绘制鼠标
        pygame.draw.circle(sur, clr, pos, 50)  # 使用随机位置画地鼠
        pygame.draw.circle(sur, (255, 0, 0), mpos, 10)  # !在鼠标位置画红色圆

    # 刷新画面
    window.blit(sur, (0, 0))
    window.blit(score_sur, (200, 10))  # 增加分数表面
    pygame.display.flip()  # 刷新画面
