# Pygame

## Pygame 简介

Pygame 是一组专门为编写游戏设计的 Python 模块，增加了 SDL 库功能。可以使你在 Python 语言中轻松的创建全功能的游戏和多媒体程序。

Pygame 是免费的，在 GPL 许可下发布，你可以创建开源，免费，免费软件，共享软件，和商业游戏。

## 安装 pygame

打开 pygame 官网下载地址：http://www.pygame.org/download.shtml

选择对应的系统版本和 python 的版本，这里我选择 pygame-1.9.1.win32-py2.7.msi 版本

![](https://upload-images.jianshu.io/upload_images/3260639-6e94acda36bb2f9c.png?imageMogr2/auto-orient/strip|imageView2/2/w/895/format/webp)

```bash
pip install pygame
```

## 开始

![pygame loop](https://upload-images.jianshu.io/upload_images/1705744-eecbfb9b78a017d6.png?imageMogr2/auto-orient/strip|imageView2/2/w/683/format/webp)

```python
# -*- coding: UTF-8 -*-

import pygame, sys
# 声明 导入pygame和sys模块，这样我们的程序才可以使用里面的方法

from pygame.locals import *
# 也是声明导入， 只是形式不同，导入所有 pygame.locals里的变量（比如下面大写的QUIT变量）


pygame.init()# 初始化pygame

DISPLAYSURF = pygame.display.set_mode((400, 300))# 设置窗口的大小单位为像素

pygame.display.set_caption('Hello World!')# 设置窗口的标题

while True: # 程序主循环

    for event in pygame.event.get():# 获取事件

        if event.type == QUIT:# 判断事件是否为退出事件

            pygame.quit()# 退出pygame

            sys.exit()# 退出系统

    pygame.display.update()# 绘制屏幕内容
```

## Pygame 常用模块

| 方法名           | 功能                       |
| ---------------- | -------------------------- |
| pygame.cdrom     | 访问光驱                   |
| pygame.display   | 访问显示设备               |
| pygame.draw      | 绘制形状、线和点           |
| pygame.cursors   | 加载光标                   |
| pygame.event     | 管理事件                   |
| pygame.font      | 使用字体                   |
| pygame.image     | 加载和存储图片             |
| pygame.joystick  | 使用游戏手柄或者类似的东西 |
| pygame.key       | 读取键盘按键               |
| pygame.mixer     | 声音                       |
| pygame.mouse     | 鼠标                       |
| pygame.movie     | 播放视频                   |
| pygame.music     | 播放音频                   |
| pygame.overlay   | 访问高级视频叠加           |
| pygame.rect      | 管理矩形区域               |
| pygame.scrap     | 本地剪贴板访问             |
| pygame.sndarray  | 操作声音数据               |
| pygame.sprite    | 操作移动图像               |
| pygame.surface   | 管理图像和屏幕             |
| pygame.surfarray | 管理点阵图像数据           |
| pygame.time      | 管理时间和帧信息           |
| pygame.transform | 缩放和移动图像             |

### cdrom 模块的常用方法

| 方法名                | 功能                                           |
| --------------------- | ---------------------------------------------- |
| pygame.cdrom.init()   | 初始化 cdrom 模块，该方法将扫描系统内所有的 CD | 设备 |
| pygame.cdrom.quit     | ()                                             | 还原 cdrom 模块，在调用该方法后，现存的任何 CD | 对象都将停止工作 |
| pygame.cdrom.get_init | ()                                             | 如果 cdrom 模块初始化完成，则返回 true，否 | 则返回 false |
| pygame.cdrom          | .get_count()                                   | 返回系统中 cd 驱动器的个数 |

### display 模块的常用方法

| 方法名                       | 功能                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| pygame.display.init()        | 初始化 display 模块                                        |
| pygame.display.quit()        | 结束 display 模块                                          |
| pygame.display.get_init()    | 如果 display 模块已经被初始化，则返回 True                 |
| pygame.display.set_mode()    | 初始化一个准备显示的界面                                   |
| pygame.display.get_surface() | 获取当前的 Surface 对象                                    |
| pygame.display.flip()        | 更新整个待显示的 Surface 对象到屏幕上                      |
| pygame.display.update()      | 更新部分内容显示到屏幕上，如果没有参数，则与 flip 功能相同 | (上一条) |

### draw 绘图

| 方法名                                                       | 功能             |
| ------------------------------------------------------------ | ---------------- |
| pygame.draw.rect(surface,color,Rect,width=0)                 | 绘制一个矩形框   |
| pygame.draw.polygon(surface,color,pointlist,width=0)         | 绘制一个         | 多边形 |
| pygame.draw.circle(surface,color,pos,radius,width=0)         | 绘制一个         | 圆 |
| pygame.draw.ellipse(surface,color,Rect,width=0)              | 绘制一个椭圆     |
| pygame.draw.arc(surface,color,Rect,start_angle,stop_angle,   | width=1)         | 绘制一条弧线 |
| pygame.draw.line(surface,color,start_pos,end_pos,width=1) 绘 | 制一条线段       |
| pygame.draw.lines(surface,color,closed,pointlist,width=1) 绘 | 制一条折线       |
| pygame.draw.aaline(surface,color,start_pos,end_pos,width=1)  | 绘制一根平滑的线 |
| pygame.draw.aalines(surface,color,closed,pointlist,width=1)  | 一系列平滑的线   |

### cursors 加载光标

| 方法名                    | 功能                         |
| ------------------------- | ---------------------------- |
| pygame.cursors.compile()  | 由纯字符串创建二进制光标数据 |
| pygame.cursors.load_xbm() | 由一个 xbm 文件载入光标数据  |

### event 事件

| 方法名                          | 功能                                       |
| ------------------------------- | ------------------------------------------ |
| pygame.event.get()              | 获取事件的返回值，使用 event.type 进行区分 |
| pygame.event.wait()             | 等待发生一个事件才会继续下去               |
| pygame.event.poll()             | 会根据现在的情形返回一个真实的事件         |
| pygame.event.set_blocked(事件名 | ) 过滤                                     |
| pygame.event.set_allowed()      | 允许事件                                   |

### 绘制文字

pygame.font.Font(filename, size)
返回一个特定字体对象，可使用该特定字体去定义文本

filename：字体文件的文件名。如果 file 参数设置为 None 则默认采用系统自带字体，如果自带字体文件无法打开就会报错。

size：字体的高 height，单位为像素；

pygame.font.Font.render(text, antialias, color, background=None)
返回一个 surface 对象（字体的渲染成的图像）

text：要显示的文字；

antialias： 为 True 时文本图像显示更光滑，为 False 时文本图像显示有锯齿状；

color：字体颜色；

background：背景颜色（可选参数），默认为小黑屏；

### image 图像

| 方法名                      | 功能                                        |
| --------------------------- | ------------------------------------------- |
| pygame.image.load()         | 从文件加载新图片                            |
| pygame.image.save()         | 将图像保存到磁盘上                          |
| pygame.image.get_extended() | 检测是否支持载入扩展的图像格式              |
| pygame.image.tostring()     | 将图像转换为字符串描述                      |
| pygame.image.fromstring()   | 将字符串描述转换为图像                      |
| pygame.image.frombuffer()   | 创建一个与字符串描述共享数据的 Surface 对象 |

## mouse 鼠标

| 方法名                     | 功能                       |
| -------------------------- | -------------------------- |
| pygame.mouse.get_pressed() | 获取鼠标按钮的状态         |
| pygame.mouse.get_pos()     | 获取鼠标光标位置           |
| pygame.mouse.get_rel()     | 获取鼠标移动的数量         |
| pygame.mouse.set_pos()     | 设置鼠标光标位置           |
| pygame.mouse.set_visible() | 隐藏或显示鼠标光标         |
| pygame.mouse.get_focused() | 检查显示是否接收了鼠标输入 |
| pygame.mouse.set_cursor()  | 为系统鼠标光标设置图像     |

### mixer 播放音频

| 方法名                            | 功能                                   |
| --------------------------------- | -------------------------------------- |
| pygame.mixer.music.load()         | 载入一个音乐文件用于播放               |
| pygame.mixer.music.play()         | 开始播放音乐流                         |
| pygame.mixer.music.rewind()       | 重新开始播放音乐                       |
| pygame.mixer.music.stop()         | 结束音乐播放                           |
| pygame.mixer.music.pause()        | 暂停音乐播放                           |
| pygame.mixer.music.unpause()      | 恢复音乐播放                           |
| pygame.mixer.music.fadeout()      | 淡出的效果结束音乐播放                 |
| pygame.mixer.music.set_volume()   | 设置音量                               |
| pygame.mixer.music.get_volume()   | 获取音量                               |
| pygame.mixer.music.get_busy()     | 检查是否正在播放音乐                   |
| pygame.mixer.music.set_pos()      | 设置播放的位置                         |
| pygame.mixer.music.get_pos()      | 获取播放的位置                         |
| pygame.mixer.music.queue()        | 将一个音乐文件放入队列中，并排在当前播 | 放的音乐之后 |
| pygame.mixer.music.set_endevent   | ()                                     | 当播放结束时发出一个事件 |
| pygame.mixer.music.get_endevent() | 获取播放结束时发送的事件               |

### Surface 对象的常用方法

| 方法名                         | 功能                                |
| ------------------------------ | ----------------------------------- |
| pygame.Surface.blit()          | 将一个图像画到另一个图像上          |
| pygame.Surface.convert()       | 转换图像的像素格式                  |
| pygame.Surface.convert_alpha() | 转化图像的像素格式，包含 alpha 通道 | 的转换 |
| pygame.Surface.fill            | ()                                  | 使用颜色填充 Surface |
| pygame.Surface.get_rect()      | 获取 Surface 的矩形区域             |

### time 时间

| 方法名                  | 功能                         |
| ----------------------- | ---------------------------- |
| pygame.time.get_ticks() | 获取以毫秒为单位的时间       |
| pygame.time.wait()      | 暂停程序一段时间             |
| pygame.time.delay()     | 暂停程序一段时间             |
| pygame.time.set_timer() | 在事件队列上重复创建一个事件 |
| pygame.time.Clock()     | 创建一个对象来帮助跟踪时间   |

### transform 缩放和移动图像

| 方法名                            | 功能                             |
| --------------------------------- | -------------------------------- |
| pygame.transform.flip             | 垂直和水平翻转                   |
| pygame.transform.scale            | 调整大小到新的分辨率             |
| pygame.transform.rotate           | 旋转图像                         |
| pygame.transform.rotozoom         | 过滤的比例和旋转                 |
| pygame.transform.scale2x          | 专业图像倍增器                   |
| pygame.transform.smoothscale      | 将表面平滑地缩放到任意大小       |
| pygame.transform.chop             | 获取内部区域已删除的图像副本     |
| pygame.transform.laplacian        | 找到表面中的边缘                 |
| pygame.transform.average_surfaces | 从许多表面找到平均表面           |
| pygame.transform.average_color    | 找到曲面的平均颜色               |
| pygame.transform.threshold        | 查找表面中的哪些像素和多少像素在 | 'search_color'或'search_surf'的阈值内 |

### Pygame 里常用的事件

| 事件            | 产生途径              | 参数              |
| --------------- | --------------------- | ----------------- |
| QUIT            | 用户按下关闭按钮      | none              |
| ACTIVEEVENT     | Pygame 被激活或者隐藏 | gain, state       |
| KEYDOWN         | 键盘被按下            | unicode, key, mod |
| KEYUP           | 键盘被放开            | key, mod          |
| MOUSEMOTION     | 鼠标移动              | pos, rel, buttons |
| MOUSEBUTTONDOWN | 鼠标按下              | pos, button       |
| MOUSEBUTTONUP   | 鼠标放开              | pos, button       |
| VIDEORESIZE     | Pygame 窗口缩放       | size, w, h        |
