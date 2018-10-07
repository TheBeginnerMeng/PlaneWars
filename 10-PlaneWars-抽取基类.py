#coding:utf-8

import pygame
import time
from pygame.locals import *
import random

class BasePlane(object):
    """docstring for BasePlane"""
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.Bullet_list = []#存储子弹
        self.Bullet_del_list = []#存储越界的子弹

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.Bullet_list:
            bullet.display()
            bullet.move()

            if bullet.judge():#判断子弹是否越界
                self.Bullet_del_list.append(bullet)

                for bullet_del in self.Bullet_del_list:
                    self.Bullet_list.remove(bullet_del)
                    self.Bullet_del_list = []

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 700, "./feiji/hero1.png")

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
    
    def fire(self):
        self.Bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.move_direction = "right"#用来存储敌机的默认方向
        
    def move(self):
        if self.move_direction == "right":
            self.x += 5
        elif self.move_direction == "left":
            self.x -= 5

        if self.x > 480-50:
            self.move_direction = "left"
        elif self.x < 0:
            self.move_direction = "right"

    def fire(self):
        random_num =  random.randint(1, 100)
        if random_num == 5 or random_num == 20:
            self.Bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(object):
    """docstring for BaseBullet"""
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y): 
        BaseBullet.__init__(self, screen_temp, x+40, y-20, "./feiji/bullet.png")

    def move(self):
        self.y-=10

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y): 
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "./feiji/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 452 :
            return True
        else:
            return False
def key_control(hero_temp):

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
                hero_temp.move_left()

            #检测是否按下了d或者Right
            elif event.key == K_d or event.key ==K_RIGHT:
                print("right")
                hero_temp.move_right()

            #检测是否按下了空格键
            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()

def main():
    #1.创建一个窗口
    screen = pygame.display.set_mode((480, 890), 0, 32)

    #2.创建一个背景图
    background = pygame.image.load("./feiji/background.png")
    
    #3.创建一个飞机对象 
    hero = HeroPlane(screen)

    #4.创建一个敌机对象
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()#敌机显示
        enemy.move()#敌机移动
        enemy.fire()#敌机开火
        pygame.display.update()
        key_control(hero)
            
        time.sleep(0.01)


if __name__ == "__main__":
    main()
