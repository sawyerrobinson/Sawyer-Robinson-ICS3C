import pygame
import random


pygame.init()

#DISPLAY
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Block Breaker")
clock = pygame.time.Clock()

#COLOURS
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (50,180,255)
YELLOW = (255,220,70)
GREEN = (70,220,120)
PURPLE = (180,100,255)


#paddle
paddle = pygame.Rect(340,540,120,15)
paddle_speed = 7


#ball
ball = pygame.Rect(390,400,16,16)
ball_x_speed = 4
ball_y_speed = -4


#main game loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False 
    screen.fill(PURPLE)







