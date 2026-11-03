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
WHITE = (255,0,0)
BLUE = (0,0,255)



#paddle
paddle = pygame.Rect(340,540,120,15)


#ball
ball = pygame.Rect(390,400,16,16)
ball_x = 4
ball_y = 4



score = 0


#bricks
bricks =[]
brick_colours = [(255,0,0)
                 (255,165,0)
                 (255,255,0)
                 (0,255,0)
                 (0,150,255)
                 (180,0,255)
                 (255,100,180)
                 (255,255,255)
                 ]

for i in range (8):
    brick = pygame.Rect (i * 100,100,80,30)
    bricks.append([brick,brick_colours[i]])




#main game loop

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #move paddle
    def move_paddle():
        keys = pygame.key.get_pressed()

        if keys [pygame.K_LEFT]:
            paddle.x -= 5

        if keys[pygame.K_RIGHT]:
            paddle.x += 5
            




    














    




    




   

    


















