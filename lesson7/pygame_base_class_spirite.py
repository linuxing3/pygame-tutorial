""" 
 小游戏标准模板 
 Sample Python/Pygame Programs

"""
from grid_backed_map import WIDTH
import random
import pygame
from pygame.locals import *

# 定义常量，比如颜色、按键等
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("alien.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()

    #  Move the sprite based on user keypresses
    def update(self, x, y):
        self.rect.move_ip(x, y)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("ufo.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = random.randint(50, 450)

    #  Move the sprite based on user keypresses
    def update(self, x, y):
        self.rect.move_ip(x, y)

def show_text(screen, text, position):
    font = pygame.font.Font(None, 36)
    over_label = font.render(text, True, GREEN)
    screen.blit(over_label, position)

def play_bmg():
    # 开始播放背景音乐
    pygame.mixer.music.load('resources/audio/moonlight.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

# 主函数
def main():
    """ 主函数 """
    # 
    ENEMYEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMYEVENT, 250)

    pygame.init()
    pygame.mixer.init()
     
    # 先搞定画布，比如尺寸、背景、标题
    size = [WIDTH, HEIGHT] = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # 状态机【1】: 完成状态
    done = False
    score = 0
    time_limit = 20

    # 状态机【2】：精灵仓库
    # 方向状态：上下左右
    keys = [False, False, False, False]
    allsprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()

    player = Player()
    players.add(player)
    allsprites.add(player)

    collision_sound = pygame.mixer.Sound("resources/audio/qubodup-crash.ogg")
    play_bmg()
    # 状态机【2】  时间、速率的状态
    clock = pygame.time.Clock()

    # -------- 不完成状态 -----------
    while not done:
        # 事件状态机开始，一般这里定义按键出发某种状态变化
        for event in pygame.event.get(): # 用户操作
            if event.type == QUIT: # 退出键
                done = True

            if event.type == ENEMYEVENT:
                enemy = Enemy()
                enemies.add(enemy)
                allsprites.add(enemy)

            if event.type == KEYDOWN: # 按下某键
                if event.key == K_w:
                    keys[0] = True
                elif event.key == K_a:
                    keys[1] = True
                elif event.key == K_s:
                    keys[2] = True
                elif event.key == K_d:
                    keys[3] = True
            if event.type == KEYUP: # 放开某键
                if event.key == K_w:
                    keys[0] = False
                elif event.key == K_a:
                    keys[1] = False
                elif event.key == K_s:
                    keys[2] = False
                elif event.key == K_d:
                    keys[3] = False
        # 事件状态机结束
     
     
        # 游戏逻辑开始，一般这里监听按键变化，更改精灵状态
        # time_limit -= 1

        # if time_limit == 0:
        #     show_text(screen, "Game Over", [WIDTH/2, HEIGHT/2])
        #     # allsprites.kill()
        #     score = 0

        # 按键监听器 Event Listener
        if keys[0]:
            player.update(0, -10)
        elif keys[2]:
            player.update(0, 10)
        if keys[1]:
            player.update(-10, 0)
        elif keys[3]:
            player.update(10, 0)

        for enemy in enemies:
            enemy.update(-20, 0)

        # 游戏逻辑结束

        # 绘图流程开始
        # 画布背景.
        screen.fill(WHITE)

        # 画出精灵
        # screen.blit(player.surf, player.rect)
        # for enemy in enemies:
        #     screen.blit(enemy.surf, enemy.rect)
        allsprites.draw(screen)

        # 显示横幅
        show_text(screen, "Hit" + str(score), [WIDTH/2, 0])

        # 检测撞击
        if pygame.sprite.spritecollide(player, enemies, True):
            collision_sound.play()
            score += 1

        # 绘图流程结束
        
        # 刷新状态
        pygame.display.flip()

        # 计时状态
        clock.tick(60)
        
    # 退出状态
    pygame.quit()

if __name__ == "__main__":
    main()
