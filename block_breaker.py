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
YELLOW = (255,220,0)
PURPLE = (128,0,128)


#paddle
paddle = pygame.Rect(340,540,120,15)
paddle_speed = 7


#ball
ball = pygame.Rect(390,400,16,16)
ball_x_speed = 4
ball_y_speed = -4


#bricks
bricks =[]
brick_colours = [RED, YELLOW, GREEN, BLUE ,PURPLE]

for row in range(5):
    for col in range(10):
        x = 25 + col * 76
        y = 70 + row * 35

        brick = pygame.Rect(x, y, 68, 25)
        colours = brick_colours[row]
        bricks.append([brick,colours])


#main game loop

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x = -6

    if keys[pygame.K_RIGHT]:
        paddle.y = 6

    if paddle.left < 0:
        paddle.left = 0

    if paddle.right > 800:
        paddle.right = 800


    #ball movement
    

    


















