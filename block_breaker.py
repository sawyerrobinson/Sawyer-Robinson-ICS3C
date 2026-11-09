import pygame
import random
import os


pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("winterfest.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)



#DISPLAY
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Block Breaker")
clock = pygame.time.Clock()



#COLOURS
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (200,16,46)
GREEN = (40,122,63)


#paddle
paddle = pygame.Rect(340,540,120,15)


#ball
ball = pygame.Rect(390,400,15,15)
ball_x = 4
ball_y = -4



score = 0


#bricks
bricks =[]
brick_colours = [RED, GREEN, RED, GREEN, RED ,GREEN, RED ,GREEN]

for i in range (8):
    brick = pygame.Rect (i * 100,100,80,30)
    bricks.append([brick,brick_colours[i]])






    #move paddle
def move_paddle():
        keys = pygame.key.get_pressed()

        if keys [pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= 8

        if keys[pygame.K_RIGHT] and paddle.right < 800:
            paddle.x += 8


    #move ball
def move_ball():
        global ball_x, ball_y
        ball.x += ball_x
        ball.y += ball_y

        #wall collisions
        if ball.left <= 0 or ball.right >= 800:
            ball_x = -ball_x

        if ball.top <= 0:
            ball_y = -ball_y

        if ball.colliderect(paddle):
            ball_y = -abs(ball_y)


#function to check when bricks are hit
def check_bricks():
    global score, ball_y

    for item in bricks[:]:
        brick_rect = item[0]
        if ball.colliderect(brick_rect):
            bricks.remove(item)
            ball_y = -ball_y
            score += 10
            break


        #draw everything
def draw_game():
    screen.fill(BLACK)

    pygame.draw.ellipse(screen,WHITE,ball)
    pygame.draw.rect(screen,BLUE,paddle)
    
    for brick in bricks:
         pygame.draw.rect(screen,brick[1],brick[0])

    #i used ai to help me make this
    font = pygame.font.SysFont(None, 35)  
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (20,20))


    pygame.display.update()

        

#main game loop
running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #game logic
    move_paddle()
    move_ball()
    check_bricks()

    #reset game if ball falls off the bottom
    if ball.bottom >= 600:
         ball.x, ball.y = 390,400
         ball_y = -4
         score = 0

    draw_game()
    pygame.display.flip()
    clock.tick(120)











    














    




    




   

    


















