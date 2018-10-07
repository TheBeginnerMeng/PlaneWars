#coding:utf-8
import pygame
import time
from pygame.locals import *

def main():
    #1.创建一个窗口
    screen = pygame.display.set_mode((480, 890), 0, 32)

    #2.创建一个背景图
    background = pygame.image.load("./feiji/background.png")
    
    #3.创建一个飞机图片 
    hero = pygame.image.load("./feiji/hero1.png")

    x = 230 
    y = 700



    while True:
        screen.blit(background, (0, 0))
        
        screen.blit(hero, (x, y))
        
        pygame.display.update()
       
        #获取事件，比如按键等
        for event in pygame.event.get():

            #判断是否点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()

            #判断是否按下了键
            elif event.type == KEYDOWN:
                #检测是否按下了a或者Left
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    x-=5

                #检测是否按下了d或者Right
                elif event.key == K_d or event.key ==K_RIGHT:
                    print("right")
                    x+=5

                #检测是否按下了空格键
                elif event.key == K_SPACE:
                    print("space")

        time.sleep(0.01)


if __name__ == "__main__":
    main()
