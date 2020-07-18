""" 
 小游戏标准模板 
 Sample Python/Pygame Programs

"""
import pygame
from pygame.locals import *
import random
import math

# 定义常量，比如颜色、按键等
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

# 先搞定画布，比如尺寸、背景、标题
size = [WIDTH, HEIGHT] = [1024, 768]

# 定义精灵类，实现初始化和更新方法


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Player, self).__init__()
        self.current_image = 0
        self.animating = False
        self.sprites = []
        self.sprites.append(pygame.image.load("resources/images/alien.png").convert())
        self.sprites.append(pygame.image.load("resources/images/alien.png").convert())
        self.sprites.append(pygame.image.load("resources/images/alien.png").convert())
        # load
        self.image = self.sprites[self.current_image]
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()
        # position
        self.rect.topleft = [pos_x, pos_y] 
        
    def animate(self):
        self.animating = True

    def update(self, x, y):
        if self.animating == True:
            self.current_image += 0.2
            # stop animating at last image
            if self.current_image > 10:
                self.current_image = 0
                self.animating = False
        # render image
        self.image = self.sprites[int(self.current_image)]
        # moving
        self.rect.move_ip(x, y)



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("resources/images/ufo.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, HEIGHT)

    def update(self, x, y):
        self.rect.move_ip(x, y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet).__init__()
        self.image = pygame.image.load("resources/images/bullet.png").convert()
        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.image.get_rect()

    def rotate(self, angle, start_x, start_y):
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def update(self, speed):
        # use angle to calculate x,y
        arc = (360 -self.angle) / 57.27
        change_x = math.cos(arc) * speed
        change_y = math.sin(arc) * speed
        self.rect.move_ip(change_x, change_y)

class Background():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("excecise_advanced/background_01.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

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
    # 自定义事件分发
    ENEMYEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMYEVENT, 250)

    # 初始化
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

    # 状态机【1】: 完成状态
    done = False
    score = 0
    time_limit = 20

    # 方向状态：上下左右
    keys = [False, False, False, False]

    # 状态机【2】：精灵仓库
    allsprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()

    bullets = []

    player = Player(100, 100)
    players.add(player)
    allsprites.add(player)

    # 
    bg = Background()
    # 音乐
    collision_sound = pygame.mixer.Sound("resources/audio/qubodup-crash.ogg")
    play_bmg()

    # 状态机【3】  时间、速率的状态
    clock = pygame.time.Clock()

    # -------- 状态机【0】 -----------
    while not done:
        # >>>
        # ==================================================================
        # 事件状态机开始，一般这里定义按键，触发某种状态变化
        for event in pygame.event.get():  # 用户操作
            if event.type == QUIT:  # 退出键
                done = True

            if event.type == ENEMYEVENT:
                enemy = Enemy()
                enemies.add(enemy)
                allsprites.add(enemy)

            if event.type == KEYDOWN:  # 按下某键
                if event.key == K_w:
                    keys[0] = True
                elif event.key == K_a:
                    keys[1] = True
                elif event.key == K_s:
                    keys[2] = True
                elif event.key == K_d:
                    keys[3] = True
                elif event.key == K_p:
                    player.animate()
            if event.type == KEYUP:  # 放开某键
                if event.key == K_w:
                    keys[0] = False
                elif event.key == K_a:
                    keys[1] = False
                elif event.key == K_s:
                    keys[2] = False
                elif event.key == K_d:
                    keys[3] = False
            if event.type == MOUSEBUTTONDOWN:
                # 计算角度
                mouse_position = pygame.mouse.get_pos()
                # 计算弧度，转化为角度，三角函数上场，1 arc =  180 / pi，因为360度就是 2 * pi的圆周
                bullet_rotate_arc = math.atan2(
                    mouse_position[1] - player.rect.y, mouse_position[0] - player.rect.x)
                bullet_rotate_angle = 360 - bullet_rotate_arc * 57.27
                print('[arrow] angel ' + str(bullet_rotate_angle))
                bullet = Bullet()
                bullet.rotate(bullet_rotate_angle, player.rect.x, player.rect.y)
                bullets.append(bullet)


        # 事件状态机结束
        # ==================================================================
        # <<<

        # >>>
        # ==================================================================
        # 游戏逻辑开始，一般这里监听按键变化，更改精灵状态
        # 状态机【4】  限时的状态
        time_limit -= 1
        if time_limit == 0:
            show_text(screen, "Game Over", [WIDTH/2, HEIGHT/2])
            # allsprites.kill()
            score = 0

        # 状态机【5】  按键监听器，更新精灵状态
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

        index = 0
        for bullet in bullets:
            x, y = bullet.rect.x, bullet.rect.y
            bullet.update(50)
            # 出界消失
            if x < -64 or x > 640 or y < -64 or y > 480:
                bullets.pop(index)
            # 撞击消失
            if pygame.sprite.spritecollide(bullet, enemies, True):
                if len(bullets) > 0:
                    collision_sound.play()
                    bullets.pop(index)
                    score += 1
            index += 1

        # 状态机【8】 精灵旋转的位置状态和角度状态
        mouse_position = pygame.mouse.get_pos()
        # 计算弧度，转化为角度，三角函数上场，1 arc =  180 / pi，因为360度就是 2 * pi的圆周
        arc = math.atan2(
            mouse_position[1] - player.rect.y, mouse_position[0] - player.rect.x)
        angle = 360 - arc * 57.27
        # rotate的第二个参数必须是角度，不是弧度
        # rotate的第一个参数是图像，而不是我们的player实例
        # rotate的返回值也是图像，可以使用get_rect方法，输出[w, h]
        rotated_player_image = pygame.transform.rotate(player.image, angle)
        ratated_player_pos = [player.rect.x - rotated_player_image.get_rect()
                       [0] / 2, player.rect.y - rotated_player_image.get_rect()[1] / 2]

        # 状态机【6】  检测撞击状态
        if pygame.sprite.spritecollide(player, enemies, False):
            collision_sound.play()
            score -= 1

        # 游戏逻辑结束
        # ==================================================================
        # <<<

        # >>>
        # ==================================================================
        # 绘图流程开始
        # 画背景
        screen.fill(WHITE)
        screen.blit(bg.image, bg.rect)

        # 画出精灵， 单独或分组画
        # screen.blit(player.surf, player.rect)
        # for enemy in enemies:
        #     screen.blit(enemy.surf, enemy.rect)
        enemies.draw(screen)

        screen.blit(rotated_player_image, ratated_player_pos)

        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
            
        # 显示横幅
        show_text(screen, "Hit" + str(score), [WIDTH/2, 0])

        # 绘图流程结束
        # ==================================================================
        # <<<

        # 刷新状态
        pygame.display.flip()

        # 计时状态
        clock.tick(60)

    # -------- 状态机【0】 -----------
    pygame.quit()


if __name__ == "__main__":
    main()
