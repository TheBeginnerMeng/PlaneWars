#coding:utf-8
import pygame
import time

def main():
    #1.创建一个窗口
    screen = pygame.display.set_mode((480, 890), 0, 32)

    #2.创建一个背景图
    background = pygame.image.load("./feiji/background.png")
    
    while True:
        screen.blit(background, (0, 0))

        pygame.display.update()
        
        time.sleep(0.01)


if __name__ == "__main__":
    main()
